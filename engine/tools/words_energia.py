"""Subtítulos de un plano de IA con el texto conocido, alineado por la energía del audio (sin Gemini).

Más fiable que clip_words.py cuando la transcripción de Gemini da tiempos amontonados (pasó en J07-J11).
Detecta los tramos con voz (umbral relativo al ruido del clip), y reparte las palabras por largo buscando
cortes en la puntuación con un ritmo de habla parejo; puede unir tramos o saltar ruidos sueltos.

Uso (desde engine/): python3 tools/words_energia.py <nombre> "<lo que dice>"   -> public/clips/<nombre>.words.json
"""
import sys,json,subprocess,numpy as np
name,text=sys.argv[1],sys.argv[2]
mp4=f'public/clips/{name}.mp4'
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',mp4,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,dtype=np.int16).astype(float)
hop=160; win=400  # 10 ms
db=np.array([20*np.log10(np.sqrt(np.mean(a[i:i+win]**2))+1) for i in range(0,len(a)-win,hop)])
db=np.convolve(db,np.ones(5)/5,'same')
thr=np.percentile(db,15)+0.5*(np.percentile(db,90)-np.percentile(db,15))
v=db>thr
segs=[];i=0
while i<len(v):
    if v[i]:
        j=i
        while j<len(v) and v[j]: j+=1
        segs.append([i*0.01,j*0.01]); i=j
    else: i+=1
m=[]
for s in segs:
    if m and s[0]-m[-1][1]<0.25: m[-1][1]=s[1]
    else: m.append(s)
segs=[s for s in m if s[1]-s[0]>=0.08]
changed=True
while changed and len(segs)>1:
    changed=False
    for i,sg in enumerate(segs):
        if sg[1]-sg[0]<0.3:
            gl=sg[0]-segs[i-1][1] if i>0 else 9
            gr=segs[i+1][0]-sg[1] if i+1<len(segs) else 9
            if min(gl,gr)>0.8: segs.pop(i)
            elif gl<=gr: segs[i-1][1]=sg[1]; segs.pop(i)
            else: segs[i+1][0]=sg[0]; segs.pop(i)
            changed=True; break
ws=text.split()
import re, math
lens=[len(w)+1 for w in ws]; W=len(ws); n=len(segs)
cum=[0]
for x in lens: cum.append(cum[-1]+x)
T=sum(b-a for a,b in segs); R=cum[-1]/T
def pen(m):
    if m==W: return 0
    w=ws[m-1]
    if re.search(r'[.?!…:]$',w): return 0
    if re.search(r'[,;]$',w): return 0.15
    return 0.6
INF=1e9
dp=[[INF]*(W+1) for _ in range(n+1)]; bk=[[None]*(W+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
    for k in range(W+1):
        if dp[i][k]>=INF: continue
        # skip segment i as noise
        c=dp[i][k]+1.0+(segs[i][1]-segs[i][0])
        if c<dp[i+1][k]: dp[i+1][k]=c; bk[i+1][k]=(i,k,None)
        for j in range(i+1,n+1):
            dur=sum(b-a for a,b in segs[i:j]); gaps=segs[j-1][1]-segs[i][0]-dur
            for m in range(k+1,W+1):
                r=(cum[m]-cum[k])/dur
                c=dp[i][k]+3*(math.log(r/R))**2*(cum[m]-cum[k])/cum[-1]*W/3+pen(m)+1.0*gaps+0.5*(j-i-1)
                if c<dp[j][m]: dp[j][m]=c; bk[j][m]=(i,k,(j,m))
runs=[];j,m=n,W
while j>0:
    i,k,t=bk[j][m]
    if t: runs.append((i,j,k,m))
    j,m=i,k
runs.reverse()
out=[]
for i,j,k,m in runs:
    sub=segs[i:j]; grp=ws[k:m]; GL=sum(len(w)+1 for w in grp); D=sum(b-a for a,b in sub)
    def at(x):
        for a_,b_ in sub:
            if x<=b_-a_+1e-9: return a_+x
            x-=b_-a_
        return sub[-1][1]
    # reparte por largo en tiempo con voz; una palabra que cruza una pausa se pasa al lado con más parte
    c=0; bounds=[]
    acc=0
    for a_,b_ in sub: acc+=b_-a_; bounds.append(acc)
    for w in grp:
        d=D*(len(w)+1)/GL; x0,x1=c,c+d*0.92
        for bnd in bounds[:-1]:
            if x0<bnd<x1:
                if bnd-x0>=x1-bnd: x1=bnd-1e-3
                else: x0=bnd+1e-3
        st=at(x0); out.append({'w':w,'s':round(st,3),'e':round(max(at(x1),st+0.05),3)}); c+=d
json.dump(out,open(f'public/clips/{name}.words.json','w'),ensure_ascii=False)
print(name,'segs',[[round(x,2) for x in s] for s in segs])
print(' '.join(f"{w['w']}@{w['s']}-{w['e']}" for w in out))
