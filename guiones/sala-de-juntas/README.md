# 50 guiones · Serie Sala de Juntas

Estructura de todos: gancho con personas hechas con IA (8 a 16 s, sala de juntas o frutinovela) y el resto en el motor con la voz del narrador. Elenco fijo: Don Ramiro (dueño), Diego (asesor flojo), Paola (asesora estrella), Andrés (sospechoso), Rubén (coordinador del Excel), Karla (agencia de marketing).

## S01 · Don Ramiro descubre el botón

_llamadas · P08 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** ¿A CUÁNTOS / LES [LLAMARON]?

**Personas con IA**

1. Plano medio de Don Ramiro de pie en la cabecera de la mesa de juntas; golpea la mesa con las dos manos, las tazas de café brincan y los asesores se echan para atrás.
   - **Don Ramiro:** "¡Doscientos leads esta semana! ¿Y a cuántos les llamaron? ¡¿A cuántos?!"
   - Sonido: golpe en la mesa, tazas que tintinean
2. Contraplano de Diego detrás de su laptop, sudando, se acomoda los lentes; Paola, a su lado, pone los ojos en blanco.
   - **Diego:** "Jefe, es que hay que buscarlos uno por uno… y se me acaba el día."
   - Sonido: silencio incómodo, un grillo

**Motor (narrador)**

- `photo` · Si tu equipo tiene que buscar lead por lead, copiar el número, marcar y anotar, al final del día llamó a quince. Y los otros ciento ochenta y cinco se enfrían.  
  Pantalla: Titular: LEAD POR [LEAD]. Foto de asesor con libreta y celular; contador 15 de 200 en rojo.
- `ui+call` · Con Lead Master tu asesor aprieta un botón y el sistema marca a toda su lista, uno tras otro. Si nadie contesta, pasa solo al siguiente.  
  Pantalla: Botón «Llamar a mi lista (200)». Insertos de llamada en cadena: Adriana Solís · no contesta → Lucía Hernández · no contesta → Diana Trejo · llamando…
- `ui+cita` · Si alguien contesta, hablas. Lo que se dijo queda en notas solo y, si agendan, la cita aparece en el calendario sin que nadie la capture.  
  Pantalla: Llamada con Diana Trejo · 3:12 min. Nota automática: «Busca 2 recámaras en Polanco, hasta 5 millones». Cita: jueves 11:00 am · confirmada.

**Cierre:** Comenta SISTEMA y te enseñamos cómo funciona.

## S02 · Diego y su CRM de papel

_llamadas · P08 · Junta · ~37 s · Comenta LEADS_

**Gancho en pantalla:** SU CRM ES UNA / [LIBRETA]

**Personas con IA**

1. Sala de juntas. Paola señala con la pluma la libreta de Diego, llena de post-its de colores y garabatos; Diego la abraza contra el pecho, orgulloso.
   - **Paola:** "Diego, ¿esa libreta es tu CRM?"
   - **Diego:** "Es mi sistema, Paola. Tiene colores."
   - Sonido: risas contenidas
2. Don Ramiro le quita la libreta a Diego y la hojea con cara de desesperación; se caen tres post-its al piso.
   - **Don Ramiro:** "Aquí dice «llamar a la señora del depa». ¿Cuál señora? ¿Cuál depa?"
   - Sonido: post-its cayendo, suspiro largo

**Motor (narrador)**

- `photo` · Cuando el seguimiento vive en una libreta, nadie sabe a quién se le llamó, a quién le toca hoy ni qué se prometió. Y si el asesor la pierde, se pierden los leads.  
  Pantalla: Foto de libreta llena de post-its. Titular: ¿CUÁL [SEÑORA]?
- `phonelist` · Con Lead Master, cada mañana tu asesor recibe en su WhatsApp la lista de a quién llamar: lo urgente, los que nunca buscó y los que se están enfriando.  
  Pantalla: Lista del día · 8:00 am: Lo urgente 3 · Nunca los has buscado 5 · Se están enfriando 4.
- `ui+note` · Y con un botón les marca a todos, uno tras otro. Lo que se habla en cada llamada queda escrito solo. Sin libreta y sin post-its.  
  Pantalla: Botón «Llamar a mi lista». Nota automática en Lucía Hernández: «Casa con jardín en Zapopan · crédito aprobado · llamarla el lunes».

**Cierre:** Comenta LEADS y te mostramos la lista del día.

## S03 · Doce llamadas en todo el día

_llamadas · P08 · Junta · ~35 s · Comenta SISTEMA_

**Gancho en pantalla:** [12] LLAMADAS / EN TODO EL DÍA

**Personas con IA**

1. Rubén, con la laptop abierta y los lentes en la punta de la nariz, lee un reporte en voz alta; Diego se va hundiendo en su silla.
   - **Rubén:** "Diego marcó a doce leads. En todo el día."
   - Sonido: teclado, carraspeo
2. Don Ramiro se levanta despacio; la cara se le pone roja y le sale vapor de las orejas como olla exprés.
   - **Don Ramiro:** "¿Doce? ¡Yo marco doce mientras se me enfría el café!"
   - Sonido: silbido de olla exprés

**Motor (narrador)**

- `flow` · El problema no siempre es que tu asesor sea flojo. Entre llamada y llamada busca el número, lo copia, marca, cuelga, anota y vuelve a empezar. Ahí se le va la mañana.  
  Pantalla: Flujo con flechas: buscar → copiar → marcar → colgar → anotar → repetir. Reloj avanzando de 9:00 a 12:30.
- `ui+call` · Con Lead Master aprieta un botón y el sistema marca solo. Si no contestan, pasa al siguiente. Si contestan, habla.  
  Pantalla: Insertos de llamada en cadena: Adriana Solís · no contesta → Lucía Hernández · no contesta → Diana Trejo · contestó.
- `compare` · Lo que antes era un día de doce llamadas se vuelve una mañana con muchos más intentos, y todo queda registrado para que tú lo veas.  
  Pantalla: Antes: 12 llamadas en el día. Con Lead Master (ejemplo): 64 intentos en la mañana · 11 contactados · 2 citas.

**Cierre:** Comenta SISTEMA y te lo mostramos funcionando.

## S04 · Plátano Diego no anotó nada

_llamadas · P08 · Frutinovela · ~36 s · Comenta CRM_

**Gancho en pantalla:** ¿QUÉ LE / [PROMETISTE]?

**Personas con IA**

1. Sala de juntas de frutas con luz de telenovela. Plátano Diego, con manchas cafés de nervios, sostiene un teléfono que suena con las dos manos.
   - **Plátano Diego:** "Lucía me está llamando… ¿qué le prometí? ¡No anoté nada!"
   - Sonido: teléfono sonando, violines dramáticos
2. Fresa Valeria, tranquila, se acomoda las hojitas de la corona y sonríe con superioridad; triple zoom dramático a su cara.
   - **Fresa Valeria:** "Yo tampoco anoto, Plátano. Mis notas se escriben solas."
   - Sonido: golpe de telenovela: ¡tan, tan, taaan!

**Motor (narrador)**

- `photo` · Tus asesores hablan con decenas de leads por semana. Nadie se acuerda de todo y casi nadie lo anota. El lead lo nota cuando le preguntas lo mismo por tercera vez.  
  Pantalla: Titular: ¿QUÉ LE [PROMETÍ]? Foto de asesor confundido mirando el celular.
- `ui+note` · Con Lead Master las llamadas salen del sistema. Cuando cuelgas, lo que se habló ya está en las notas: qué busca, cuánto puede pagar y qué le prometiste.  
  Pantalla: Nota automática en Lucía Hernández: «Casa de 3 recámaras en Zapopan · hasta 4.5 millones · crédito bancario · prometí mandarle 3 opciones el martes».
- `ui+crm` · Así cualquier asesor retoma la conversación donde se quedó, y tú ves qué se le dijo a cada cliente sin preguntarle a nadie.  
  Pantalla: Ficha del lead con historial: llamada de 4:05 min, nota, siguiente paso «mandar opciones el martes».

**Cierre:** Comenta CRM y te mostramos cómo se llenan solas las notas.

## S05 · Llegó a su cita y nadie sabía

_llamadas · P08 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** LLEGÓ A SU CITA / Y NADIE [SABÍA]

**Personas con IA**

1. Don Ramiro entra de golpe a la sala de juntas con los brazos abiertos, señalando hacia la recepción a través de la puerta de vidrio.
   - **Don Ramiro:** "¡Hay un cliente en recepción que dice que tiene cita! ¿Quién lo agendó?"
   - Sonido: puerta que se abre, murmullos
2. Andrés, recargado con su chamarra de cuero, esconde el celular rápido y levanta la mano a medias.
   - **Andrés:** "Yo, jefe. La agendé… en mi cabeza."
   - Sonido: silencio, alguien se ríe bajito

**Motor (narrador)**

- `photo` · Cuando las citas se apuntan en el celular de cada asesor, nadie más se entera. El cliente llega, nadie lo atiende y se va pensando que tu inmobiliaria es un desorden.  
  Pantalla: Titular: AGENDADA EN SU [CABEZA]. Foto de recepción vacía.
- `ui+cita` · Con Lead Master tu asesor llama desde el sistema. Si en la llamada acuerdan una visita, la cita se crea sola en el calendario de tu CRM, como GoHighLevel.  
  Pantalla: Llamada con Diana Trejo: «nos vemos el sábado a las 11». Inserto de cita: sábado 11:00 am · Recorrido Torre Polanco · Andrés M. · confirmada.
- `ui+report` · Todo el equipo la ve, a ti te aparece en el reporte del día y el cliente llega a una oficina que ya lo está esperando.  
  Pantalla: Reporte del equipo: Citas de mañana: 5 · sábado 11:00 Diana Trejo (Andrés M.).

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S06 · 3,000 leads en la pestaña «Ya no»

_llamadas · P08 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** [3,000] LEADS / OLVIDADOS

**Personas con IA**

1. Don Ramiro de pie frente a una pantalla que proyecta un Excel enorme con miles de filas; voltea furioso hacia la mesa.
   - **Don Ramiro:** "Tenemos tres mil leads viejos en este Excel. ¿Alguien les ha vuelto a marcar?"
   - Sonido: zumbido de proyector
2. Todos miran al techo. Rubén, sin levantar la vista de su laptop, se sube los lentes con un dedo.
   - **Rubén:** "Están en la pestaña que se llama «Ya no», jefe."
   - Sonido: grillos

**Motor (narrador)**

- `stat` · Esos leads ya los pagaste. Muchos no compraron porque nadie les volvió a llamar, no porque no quisieran.  
  Pantalla: Número gigante: 3,000 leads · ya pagados · 0 llamadas este año.
- `ui+call` · Con Lead Master tu base vieja queda en una lista. Tu equipo aprieta un botón y el sistema les marca uno tras otro. El que no contesta se salta; el que contesta, habla con tu asesor.  
  Pantalla: Botón «Llamar a la lista: Base 2024 (3,000)». Insertos de llamada en cadena.
- `ui+report` · Lo que se habla queda en notas y las citas se agendan solas. Con un solo día de reactivación sabes cuántos de esos leads siguen buscando.  
  Pantalla: Resumen del día de reactivación (ejemplo): 412 llamadas · 96 contestaron · 18 siguen buscando · 6 citas.

**Cierre:** Comenta LEADS y te decimos cómo reactivar tu base.

## S07 · «Vamos súper bien, jefe»

_chat · P09 · Junta · ~34 s · Comenta SISTEMA_

**Gancho en pantalla:** «SÚPER BIEN, / [JEFE]»

**Personas con IA**

1. Junta de los lunes. Don Ramiro, con los brazos cruzados, mira fijo a Diego; Diego sonríe demasiado.
   - **Don Ramiro:** "Diego, ¿cómo vamos con los leads de hoy?"
   - **Diego:** "¡Súper bien, jefe! A todos les marqué."
   - Sonido: reloj de pared
2. Don Ramiro saca su celular, lee la pantalla despacio y levanta una ceja; a Diego se le borra la sonrisa.
   - **Don Ramiro:** "Aquí dice que le marcaste a dos. De veintiocho."
   - Sonido: disco rayado

**Motor (narrador)**

- `photo` · Si para saber qué hizo tu equipo tienes que preguntarle a cada asesor, te van a contestar lo que quieres oír.  
  Pantalla: Titular: TE DICEN LO QUE QUIERES [OÍR].
- `chat` · En Lead Master le escribes al sistema como a una persona: ¿quién no ha llamado a sus leads de hoy? Y te contesta con lo que pasó en los chats y en las llamadas.  
  Pantalla: Chat con la IA de Lead Master. Pregunta: «¿Quién no ha llamado a sus leads de hoy?». Respuesta: «Diego H.: 2 de 28. Andrés M.: 9 de 22. Paola G. y Valeria R.: todos contactados.»
- `ui+tasks` · Sin juntas eternas y sin Excel. Preguntas, te responde y sabes a quién tienes que apoyar hoy.  
  Pantalla: Inserto: los 26 leads de Diego sin llamada, ordenados del más antiguo al más reciente.

**Cierre:** Comenta SISTEMA y te enseñamos el chat.

## S08 · Lo que Plátano le prometió a Diana

_chat · P09 · Frutinovela · ~36 s · Comenta LEADS_

**Gancho en pantalla:** NO SE ACUERDA / DE [NADA]

**Personas con IA**

1. Sala de juntas de frutas con luz de telenovela. Don Piña, con la corona temblando de coraje, de pie frente a Plátano Diego.
   - **Don Piña:** "¡Diana Trejo está furiosa! Dice que le prometiste algo. ¿Qué le prometiste, Plátano?"
   - Sonido: trueno, violines
2. Plátano Diego tartamudea y mira a todos lados; Aguacate Andrés se esconde detrás de una maceta; zoom dramático a Plátano.
   - **Plátano Diego:** "¿Prometer? Yo nunca prometo nada… creo… a veces."
   - Sonido: golpe de telenovela: ¡tan, tan, taaan!

**Motor (narrador)**

- `photo` · Pasa en todas las inmobiliarias: el cliente se acuerda de todo lo que le dijeron. Tu asesor no.  
  Pantalla: Titular: EL CLIENTE SÍ SE [ACUERDA].
- `chat` · Con Lead Master, el asesor le pregunta al sistema: ¿qué le prometí a Diana Trejo? La IA revisa sus chats y sus llamadas y le contesta en segundos.  
  Pantalla: Chat. Pregunta: «¿Qué le prometí a Diana Trejo?». Respuesta: «El 3 de noviembre le prometiste mandarle opciones en Polanco hasta 5 millones y llamarla el jueves. Todavía no se hace ninguna de las dos.»
- `phonelist` · Y como ya está en su lista del día, no se le vuelve a pasar. El cliente siente que lo escuchaste, aunque hayas tenido cuarenta chats esa semana.  
  Pantalla: Lista del día: Lo urgente · Diana Trejo · «mandar opciones en Polanco y llamar hoy».

**Cierre:** Comenta LEADS y te mostramos cómo le preguntas al sistema.

## S09 · El reporte de catorce pestañas

_chat · P09 · Junta · ~35 s · Comenta SISTEMA_

**Gancho en pantalla:** UN REPORTE DE / [14] PESTAÑAS

**Personas con IA**

1. Rubén, orgulloso, proyecta un Excel con catorce pestañas de colores; tiene un control de presentaciones en la mano.
   - **Rubén:** "Jefe, el reporte de la semana. Son catorce pestañas, empiezo por la de colores."
   - Sonido: clic de presentador
2. Don Ramiro, agotado, apoya la frente en la mesa y levanta un solo dedo sin levantar la cabeza.
   - **Don Ramiro:** "Rubén. Yo solo quiero saber una cosa: ¿quién sacó citas esta semana?"
   - Sonido: suspiro largo

**Motor (narrador)**

- `photo` · Tu coordinador tarda días armando un reporte que nadie lee, porque tú solo quieres contestar una o dos preguntas.  
  Pantalla: Titular: 4 DÍAS PARA UN [REPORTE]. Foto de Excel de noche.
- `chat` · En Lead Master se lo preguntas directo: ¿cuántas citas salieron esta semana y de qué asesor? Y te contesta con los datos de los chats y las llamadas, sin que nadie llene nada.  
  Pantalla: Chat. Pregunta: «¿Cuántas citas salieron esta semana y de quién?». Respuesta: «19 citas: Paola G. 7 · Valeria R. 6 · Andrés M. 4 · Diego H. 2.»
- `bars` · Una pregunta en lugar de catorce pestañas. Y tu coordinador deja de armar reportes y se pone a ayudar a vender.  
  Pantalla: Barras de citas por asesor: Paola 7, Valeria 6, Andrés 4, Diego 2.

**Cierre:** Comenta SISTEMA y hazle tu primera pregunta.

## S10 · El mensaje del domingo a las 11 pm

_chat · P09 · Junta · ~34 s · Comenta SISTEMA_

**Gancho en pantalla:** DOMINGO, / [11] PM

**Personas con IA**

1. Lunes en la sala de juntas. Don Ramiro, despeinado y ojeroso, levanta su celular y muestra un chat de grupo lleno de mensajes suyos sin respuesta.
   - **Don Ramiro:** "¡El domingo a las once pregunté cuántas citas teníamos hoy! ¡Nadie contestó!"
   - Sonido: ráfaga de notificaciones de WhatsApp
2. Diego y Paola se miran; Paola contesta sin despegar la vista de su café.
   - **Diego:** "Jefe… era domingo."
   - **Paola:** "Y eran las once."
   - Sonido: sorbo de café

**Motor (narrador)**

- `photo` · Si para saber cómo viene tu semana tienes que escribirle a tu equipo en domingo, el problema no es tu equipo. Es que la información vive en sus celulares.  
  Pantalla: Titular: LA INFORMACIÓN VIVE EN SUS [CELULARES].
- `chat` · Con Lead Master le preguntas al sistema desde tu celular, a la hora que quieras: ¿qué citas tenemos el lunes? ¿Qué leads entraron el fin de semana y quién los tiene?  
  Pantalla: Chat · domingo 23:04. «¿Qué citas tenemos mañana?» → «5 citas: 10:00 Diana Trejo (Paola G.) · 12:00 Lucía Hernández (Valeria R.)…». «¿Qué leads entraron el fin de semana?» → «23, todos asignados; 4 sin contacto (Diego H.)».
- `photo` · Tú duermes tranquilo, tu equipo descansa y el lunes la junta dura diez minutos.  
  Pantalla: Foto de dueño relajado. Titular: LA JUNTA DURA [10] MINUTOS.

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S11 · ¿Quién no llamó hoy? Don Ramiro le pregunta a la IA

_chat · P09 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** ¿QUIÉN NO / [LLAMÓ] HOY?

**Personas con IA**

1. Plano medio de Don Ramiro de pie en la cabecera de la mesa, mirando a cada asesor con los ojos entrecerrados.
   - **Don Ramiro:** "A ver. Que levante la mano el que NO llamó a sus leads hoy."
   - Sonido: silencio tenso, reloj de pared
2. Diego, Andrés y Paola con los brazos cruzados; Don Ramiro voltea su celular hacia Diego y sonríe.
   - **Diego:** "¡Yo llamé a todos, jefe! A todititos."
   - **Don Ramiro:** "Qué raro. La IA dice que hiciste dos llamadas."
   - Sonido: grillos

**Motor (narrador)**

- `photo` · En casi todas las juntas pasa lo mismo: preguntas quién hizo su trabajo y todos dicen que sí. Y tú no tienes cómo comprobarlo sin revisar celular por celular.  
  Pantalla: Foto de junta con asesores. Titular: TODOS DICEN QUE [SÍ].
- `mock` · Con Lead Master le escribes al sistema como a una persona: ¿quién no llamó a sus leads hoy? Y te contesta en segundos, con nombres y números.  
  Pantalla: Chat con la IA de Lead Master. Pregunta: «¿Quién no llamó a sus leads hoy?». Respuesta: «Diego H.: 2 de 14 leads. Andrés M.: 5 de 11. Paola G.: 12 de 12.»
- `ui+report` · Lo sabe porque vive en el WhatsApp y en las llamadas de cada asesor. Nadie tiene que llenar nada para que tú tengas la respuesta.  
  Pantalla: Inserto report: «Hoy: 37 leads asignados · 9 sin llamada (Diego H. 6, Andrés M. 3) · 5 citas».

**Cierre:** Comenta SISTEMA y te enseño el chat por dentro.

## S12 · Plátano Diego no se acuerda qué le prometió a Lucía

_chat · P09 · Frutinovela · ~35 s · Comenta LEADS_

**Gancho en pantalla:** ¿QUÉ LE / [PROMETISTE]?

**Personas con IA**

1. Sala de juntas de frutas con música de telenovela. Plátano Diego contesta el celular, se pone pálido y tapa la bocina con la mano.
   - **Plátano Diego:** "¡Es Lucía Hernández! ¿Qué le prometí? ¿¡Qué le prometí la semana pasada!?"
   - Sonido: música dramática, celular vibrando
2. Fresa Valeria, sentada a su lado, le quita el celular con calma y empieza a teclear; triple zoom dramático a Plátano.
   - **Fresa Valeria:** "Tranquilo, Plátano. Le preguntamos al sistema."
   - **Plátano Diego:** "¿El sistema se acuerda mejor que yo?"
   - Sonido: trueno, golpe de piano

**Motor (narrador)**

- `photo` · Tu asesor habla con cuarenta leads a la semana. Es imposible que se acuerde de lo que le prometió a cada uno. Y el lead sí se acuerda.  
  Pantalla: Foto de asesor con el celular lleno de chats. Titular: EL LEAD SÍ SE [ACUERDA].
- `mock` · En Lead Master el asesor pregunta: ¿qué le prometí a Lucía Hernández? Y la IA le contesta con lo que se habló en el chat y en la llamada.  
  Pantalla: Chat con la IA. Pregunta: «¿Qué le prometí a Lucía Hernández?». Respuesta: «Mandarle 3 opciones en Del Valle hasta 4.5 millones y llamarla el jueves a las 6 pm. Le preocupa el crédito.»
- `ui+note` · Todo eso queda escrito solo, de cada chat y de cada llamada. Tu asesor contesta seguro y el lead siente que lo están atendiendo de verdad.  
  Pantalla: Inserto note: «Nota de la IA · Lucía Hernández · 3 opciones en Del Valle · llamar jueves 6 pm · duda: crédito».

**Cierre:** Comenta LEADS y te mando cómo funciona.

## S13 · «Nadie contesta», dijo Diego. Los números no

_metricas · P10 · Junta · ~37 s · Comenta LEADS_

**Gancho en pantalla:** NADIE / [CONTESTA]

**Personas con IA**

1. Diego de pie frente a la mesa, con los brazos abiertos, indignado; golpea la mesa con la palma.
   - **Diego:** "¡Jefe, esos leads no sirven! ¡Nadie contesta! ¡Nadie!"
   - Sonido: golpe en la mesa
2. Don Ramiro voltea despacio hacia Paola, que levanta la mirada de su laptop con una ceja arriba.
   - **Don Ramiro:** "¿Y a ti, Paola?"
   - **Paola:** "A mí me contestan cuatro de cada diez. Los mismos leads."
   - Sonido: silencio incómodo

**Motor (narrador)**

- `photo` · Cuando un asesor dice que nadie contesta, casi siempre le crees. Y le echas la culpa a la campaña, al portal o a Meta.  
  Pantalla: Foto de asesor frustrado con el celular. Titular: ¿CULPA DEL [LEAD]?
- `bars` · Lead Master mide la tasa de contestación de cada asesor. Si con los mismos leads a Paola le contestan cuatro de cada diez y a Diego uno, el problema no es el lead.  
  Pantalla: Barras de tasa de contestación: Paola G. 41 % · Valeria R. 37 % · Diego H. 9 %.
- `stack` · Y te enseña por qué: cuántos intentos hizo, a qué hora llamó y cuánto duró cada llamada. Así sabes si tienes que cambiar la campaña o hablar con tu asesor.  
  Pantalla: Tarjetas sobre Diego H.: «1 intento por lead» · «Llama de 1 a 3 pm» · «Llamadas de 8 segundos».

**Cierre:** Comenta LEADS y te enseño la tasa de tu equipo.

## S14 · Diego llama a la hora de la comida. Todos los días

_metricas · P10 · Junta · ~35 s · Comenta LEADS_

**Gancho en pantalla:** ¿A QUÉ HORA / [LLAMAS]?

**Personas con IA**

1. Diego en la sala de juntas con la boca llena, mordiendo una torta enorme y marcando con la otra mano.
   - **Diego:** "Son las dos y media, jefe. Hora perfecta para llamar."
   - Sonido: mordida, tono de llamada que nadie contesta
2. Don Ramiro, rojo de coraje, señala la torta con el dedo tembloroso.
   - **Don Ramiro:** "¡A esta hora tus clientes también están comiendo, Diego! ¡Como tú!"
   - Sonido: golpe en la mesa

**Motor (narrador)**

- `photo` · Tu equipo llama cuando tiene tiempo, no cuando el cliente puede contestar. Y luego te dice que los leads no contestan.  
  Pantalla: Foto de asesor comiendo en su escritorio. Titular: LLAMAN CUANDO [PUEDEN].
- `bars` · Lead Master te muestra a qué hora te contestan más tus leads. En este ejemplo contestaban el triple entre siete y nueve de la noche, justo cuando nadie llamaba.  
  Pantalla: Barras por hora (datos de ejemplo): 9 am 18 % · 2 pm 7 % · 7 pm 39 % · 8 pm 34 %.
- `ui+tasks` · ¿Por qué te importa? Porque mover las llamadas a la hora correcta sube las contestaciones sin pagar un solo lead más.  
  Pantalla: Inserto tasks: lista del día de Diego: «7:00 pm · llamar a Adriana Solís, Diana Trejo y Lucía Hernández».

**Cierre:** Comenta LEADS y te digo a qué hora te contestan.

## S15 · 61 llamadas de 7 segundos: el récord de Andrés

_metricas · P10 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** 61 LLAMADAS / DE [7] SEGUNDOS

**Personas con IA**

1. Andrés se pone de pie y presume con el celular en alto mientras los demás aplauden sin ganas.
   - **Andrés:** "Sesenta y una llamadas ayer. Soy el que más llamó de toda la oficina."
   - Sonido: aplausos flojos
2. Rubén se baja los lentes a la punta de la nariz y lee su laptop; Don Ramiro abre los ojos enormes.
   - **Rubén:** "Sesenta y una… de siete segundos cada una."
   - **Don Ramiro:** "¿Siete segundos? ¡Eso ni es un hola!"
   - Sonido: disco rayado

**Motor (narrador)**

- `photo` · Contar llamadas no sirve de nada si no sabes cuánto duraron ni cuántas veces se intentó de verdad con cada lead.  
  Pantalla: Foto de asesor marcando sin parar. Titular: ¿LLAMADAS O [MARCADAS]?
- `panel` · Lead Master te muestra por asesor cuántas llamadas hizo, cuánto duraron y cuántos intentos hubo por lead. Ahí ves quién de verdad está hablando con clientes.  
  Pantalla: Panel: Paola G. · 38 llamadas · 3:40 min promedio · 3 intentos por lead | Andrés M. · 61 llamadas · 0:07 min promedio · 1 intento por lead.
- `compare` · ¿Por qué importa? Porque una llamada de siete segundos no vende ningún departamento. Una conversación de cuatro minutos sí agenda una visita con un cliente.  
  Pantalla: Antes: «Andrés: 61 llamadas» (se ve increíble). Con Lead Master: «61 llamadas · 0 conversaciones · 0 citas».

**Cierre:** Comenta SISTEMA y te enseño las llamadas de tu equipo.

## S16 · El lead preguntó a las 10:02. Diego contestó a las 4:15

_metricas · P10 · Junta · ~37 s · Comenta LEADS_

**Gancho en pantalla:** SEIS HORAS / PARA [CONTESTAR]

**Personas con IA**

1. Don Ramiro lee su celular en voz alta, con una calma que da miedo, de pie junto a Diego.
   - **Don Ramiro:** "La señora preguntó a las diez de la mañana. ¿A qué hora le contestaste?"
   - Sonido: reloj de pared con tic tac fuerte
2. Diego mira al techo, cuenta con los dedos y sonríe nervioso.
   - **Diego:** "A las cuatro… y cuarto. Pero le contesté con mucho cariño, jefe."
   - Sonido: grillos

**Motor (narrador)**

- `photo` · Un lead que pregunta por un departamento está preguntando en otras tres inmobiliarias al mismo tiempo. El primero que contesta se queda con la conversación.  
  Pantalla: Foto de mujer con el celular comparando chats. Titular: EL PRIMERO [GANA].
- `panel` · Lead Master mide el tiempo de respuesta de cada asesor, desde que entra el lead hasta el primer mensaje o la primera llamada.  
  Pantalla: Panel de tiempo de primera respuesta: Paola G. 6 min · Valeria R. 14 min · Diego H. 6 h 13 min.
- `ui+report` · Y si un lead se queda sin atender, pasa al siguiente asesor y a ti te llega el aviso. ¿Por qué importa? Porque cada hora de espera es un comprador que se enfría.  
  Pantalla: Inserto report: «Aviso: Diana Trejo lleva 2 h sin respuesta (Diego H.) → reasignada a Paola G.».

**Cierre:** Comenta LEADS y te enseño cuánto tarda tu equipo.

## S17 · Los 23 leads que nadie tocó en la Inmobiliaria Frutal

_metricas · P10 · Frutinovela · ~36 s · Comenta LEADS_

**Gancho en pantalla:** 23 LEADS / [SIN] CONTACTO

**Personas con IA**

1. Sala de juntas de frutas con música de telenovela. Limón abre la laptop despacio, con mirada fría, frente a Don Piña.
   - **Limón:** "Don Piña… hay veintitrés leads que nadie ha tocado. Ni un mensaje."
   - Sonido: música dramática, trueno
2. Don Piña voltea lentamente hacia Plátano Diego, que se esconde detrás de una taza; triple zoom a su cara.
   - **Don Piña:** "¿De quién son esos leads, Plátano?"
   - **Plátano Diego:** "¿Míos? ¿Todos? Qué coincidencia."
   - Sonido: triple zoom, golpe de piano

**Motor (narrador)**

- `photo` · En casi todas las inmobiliarias hay leads que entraron, se asignaron y nadie les escribió nunca. Y el dueño no se entera, porque nadie lo reporta.  
  Pantalla: Foto de bandeja de WhatsApp con mensajes sin leer. Titular: NADIE LES [ESCRIBIÓ].
- `stat` · Lead Master te dice cuántos leads están sin contacto hoy, de qué asesor son y desde cuándo están esperando.  
  Pantalla: Número gigante: 23 sin contacto · Diego H. 17 · Andrés M. 6.
- `ui+tasks` · Esos leads suben solos a la lista urgente del asesor por WhatsApp. ¿Por qué importa? Porque ya pagaste por cada uno, y un lead sin contacto es dinero tirado.  
  Pantalla: Inserto tasks: lista de Diego por WhatsApp: «Lo urgente: 17 leads que nunca has buscado».

**Cierre:** Comenta LEADS y te digo cuántos tienes sin tocar.

## S18 · 400 leads de Facebook vs. 40 del portal: ¿cuál vende?

_metricas · P10 · Junta · ~37 s · Comenta LEADS_

**Gancho en pantalla:** ¿DE DÓNDE / SALEN LAS [CITAS]?

**Personas con IA**

1. Karla de pie junto a una pantalla con una gráfica que sube, sonriendo de oreja a oreja.
   - **Karla:** "¡Cuatrocientos leads este mes, a tres dólares! ¡La mejor campaña del año!"
   - Sonido: fanfarria corta
2. Paola, sin levantar la vista del celular, la interrumpe; Don Ramiro voltea a verla con la boca abierta.
   - **Paola:** "Y dos citas. Las otras nueve salieron del portal."
   - **Don Ramiro:** "¿Y entonces a quién le estamos pagando?"
   - Sonido: disco rayado

**Motor (narrador)**

- `photo` · Contar cuántos leads te trae cada canal no sirve. Lo que importa es cuántas citas y cuántos apartados salen de cada uno.  
  Pantalla: Foto de dueño frente a una gráfica de anuncios. Titular: LEADS NO SON [CITAS].
- `bars` · Lead Master te muestra las citas por fuente: anuncios, portales y referidos. Así ves qué canal trae compradores y cuál te trae puros curiosos.  
  Pantalla: Barras (datos de ejemplo): Facebook 400 leads → 2 citas · Inmuebles24 40 leads → 9 citas · Referidos 12 leads → 4 citas.
- `compare` · ¿Por qué importa? Porque así mueves tu presupuesto a lo que sí vende. Y Lead Master le avisa a Meta quién sí agendó, para que te traiga más gente así.  
  Pantalla: Antes: «Costo por lead: US$3». Con Lead Master: «Costo por cita: Facebook US$600 · Inmuebles24 US$45».

**Cierre:** Comenta LEADS y te enseño de dónde salen tus citas.

## S19 · ¿Por qué no compran? Rubén tendría que oír 300 llamadas

_objeciones · P10 · Junta · ~37 s · Comenta SISTEMA_

**Gancho en pantalla:** ¿POR QUÉ NO / [COMPRAN]?

**Personas con IA**

1. Don Ramiro golpea la mesa con una carpeta gruesa; todos brincan en sus sillas.
   - **Don Ramiro:** "¡Trescientos leads y tres ventas! ¿Por qué carajo no nos compran?"
   - Sonido: golpe de carpeta
2. Rubén se ajusta los lentes y voltea la laptop hacia Don Ramiro, muy serio.
   - **Rubén:** "Para saberlo habría que escuchar las trescientas llamadas, jefe."
   - **Don Ramiro:** "¡Pues escúchalas!"
   - Sonido: Rubén traga saliva

**Motor (narrador)**

- `photo` · Nadie en tu equipo tiene tiempo de escuchar cientos de llamadas para entender por qué no te compran. Así que adivinas.  
  Pantalla: Foto de coordinador con audífonos y una pila de papeles. Titular: ¿Y SI SOLO [ADIVINAS]?
- `bars` · Lead Master detecta las objeciones en los chats y en las llamadas, y te dice cuáles se repiten más: precio, ubicación, crédito y el famoso «lo voy a pensar».  
  Pantalla: Barras (datos de ejemplo): «Está muy caro» 34 % · «No califico al crédito» 27 % · «Lo voy a pensar» 21 % · «Está muy lejos» 18 %.
- `stack` · Si el veintisiete por ciento no califica al crédito, no necesitas más leads. Necesitas un aliado hipotecario y una respuesta preparada para esa objeción.  
  Pantalla: Tarjetas: «Crédito: invita al asesor hipotecario a la primera llamada» · «Precio: muestra planes de pago» · «Lo voy a pensar: agenda la visita con fecha».

**Cierre:** Comenta SISTEMA y te enseño las objeciones de tus clientes.

## S20 · «Lo voy a pensar»: la frase que Diego siempre acepta

_objeciones · P10 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** «LO VOY A / [PENSAR]»

**Personas con IA**

1. Diego habla por el celular en altavoz sobre la mesa de juntas; sonríe tranquilo y cuelga.
   - **Diego:** "Perfecto, señora. Piénselo con calma, yo aquí la espero."
   - Sonido: tono de llamada colgada
2. Paola y Don Ramiro voltean a ver a Diego al mismo tiempo, incrédulos.
   - **Paola:** "Es la quinta de hoy que se va a pensarlo."
   - **Diego:** "Es que la gente piensa mucho, Paola."
   - Sonido: grillos

**Motor (narrador)**

- `photo` · «Lo voy a pensar» casi nunca significa que lo va a pensar. Significa que tiene una duda que nadie le preguntó.  
  Pantalla: Foto de clienta dudando con el celular en la mano. Titular: NO LO VA A [PENSAR].
- `bars` · Lead Master junta las objeciones de todos los chats y llamadas de tu equipo. Si «lo voy a pensar» es la número uno, ya sabes qué entrenar en la próxima junta.  
  Pantalla: Barras (datos de ejemplo): «Lo voy a pensar» 38 % · Precio 26 % · Ubicación 19 % · Crédito 17 %.
- `compare` · Antes, cada asesor aceptaba la frase y colgaba. Ahora que sabes que es la objeción más común, entrenas a tu equipo con una sola pregunta: ¿qué le falta para decidirse?  
  Pantalla: Antes: «5 leads se quedaron pensando». Con Lead Master: «Objeción número 1 del equipo: lo voy a pensar · Respuesta: ¿qué le falta para decidirse?».

**Cierre:** Comenta SISTEMA y te enseño qué objeciones escucha tu equipo.

## S21 · Treinta citas y cero apartados

_objeciones · P10 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** 30 CITAS, / [0] APARTADOS

**Personas con IA**

1. Plano medio de Don Ramiro en la cabecera de la sala de juntas; avienta una hoja impresa sobre la mesa y se le pone la cara roja.
   - **Don Ramiro:** "¡Treinta citas este mes y cero apartados! ¿Qué carajo les están diciendo los clientes?"
   - Sonido: hoja golpeando la mesa, tazas que brincan
2. Plano general de la mesa: Diego contesta rápido y nervioso; Rubén, muy serio, gira su laptop con un Excel enorme hacia Don Ramiro.
   - **Diego:** "Que está caro, jefe."
   - **Rubén:** "Según mi Excel, la objeción número uno es… «otros»."
   - Sonido: silencio incómodo, un grillo

**Motor (narrador)**

- `photo` · Si nadie sabe por qué no compran tus clientes, cada asesor adivina. Y con adivinanzas no se corrige nada.  
  Pantalla: Foto de una junta tensa. Titular: ¿POR QUÉ NO [COMPRAN]?
- `bars` · Lead Master lee los chats y las llamadas de tu equipo y te muestra las objeciones más comunes de tus clientes: precio, ubicación, crédito y el famoso «lo voy a pensar».  
  Pantalla: Barras «Objeciones del mes»: Precio 41 %, Ubicación 22 %, Crédito 18 %, «Lo voy a pensar» 12 %, Otras 7 %.
- `compare` · Así sabes qué corregir. Si es precio, ajustas el anuncio. Si es crédito, capacitas al equipo. Y dejas de culpar al cliente.  
  Pantalla: Antes: «otros» en el Excel de Rubén. Con Lead Master: objeción número uno, precio, 41 % de las conversaciones.

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S22 · Fresa Valeria y los veinte «lo voy a pensar»

_objeciones · P10 · Frutinovela · ~38 s · Comenta LEADS_

**Gancho en pantalla:** «LO VOY A / [PENSAR]»

**Personas con IA**

1. Sala de juntas de frutas con música de telenovela; zoom lento a Fresa Valeria, que llora lágrimas de jugo.
   - **Fresa Valeria:** "Don Piña… los veinte clientes de esta semana me dijeron lo mismo: «lo voy a pensar»."
   - Sonido: violines dramáticos
2. Triple zoom a Don Piña, a quien se le paran las hojas de la corona; al fondo, Plátano Diego levanta la mano muy tranquilo.
   - **Don Piña:** "¡¿Veinte?! ¿Y cuántos lo pensaron?"
   - **Plátano Diego:** "Yo tampoco lo pensé, Don Piña."
   - Sonido: trueno, golpe de orquesta

**Motor (narrador)**

- `photo` · «Lo voy a pensar» no es un no. Es una objeción que nadie le preguntó al cliente. Y si no la mides, la escuchas todas las semanas.  
  Pantalla: Titular: «LO VOY A PENSAR» [NO ES UN NO]. Foto de asesora con el celular.
- `panel` · Lead Master revisa los chats y las llamadas de tu equipo y te dice qué objeciones se repiten más. Aquí, «lo voy a pensar» va en primer lugar.  
  Pantalla: Panel «Objeciones del mes»: «Lo voy a pensar» 34 %, Precio 27 %, Crédito 19 %, Ubicación 12 %.
- `phonelist` · Y como cada asesor recibe su lista del día, esos clientes no se quedan pensando solos: les toca llamada antes de que se enfríen.  
  Pantalla: Celular de Valeria, «Tu lista de hoy · 8:00 am»: Se están enfriando (6) · Diana Trejo: «lo voy a pensar», hace 3 días.

**Cierre:** Comenta LEADS y te lo instalamos.

## S23 · ¿Quién sabe de crédito Infonavit?

_objeciones · P10 · Junta · ~37 s · Comenta INMOBILIARIO_

**Gancho en pantalla:** ¿QUIÉN SABE DE / [CRÉDITO]?

**Personas con IA**

1. Don Ramiro de pie junto a un pizarrón con la palabra CRÉDITO escrita enorme; mira a todos con los brazos cruzados.
   - **Don Ramiro:** "Uno de cada tres clientes pregunta por crédito Infonavit. ¿Quién sabe cómo funciona?"
   - Sonido: marcador rechinando en el pizarrón
2. Silencio total; Diego levanta la mano despacio, muy serio. Paola se tapa la cara con las dos manos.
   - **Diego:** "Jefe… ¿se come?"
   - Sonido: grillos, Don Ramiro suspira fuerte

**Motor (narrador)**

- `photo` · Si tus clientes preguntan por crédito y tu equipo no sabe contestar, no es que no tengan dinero. Es que nadie les resolvió la duda.  
  Pantalla: Titular: NADIE LES [RESOLVIÓ] LA DUDA. Foto de pareja revisando papeles.
- `bars` · Lead Master saca de los chats y las llamadas las objeciones más comunes de tus clientes. En esta inmobiliaria, el crédito aparece en casi uno de cada tres.  
  Pantalla: Barras «Objeciones del mes»: Crédito 31 %, Precio 26 %, Ubicación 17 %, «Lo voy a pensar» 15 %.
- `flow` · Con ese dato sabes qué hacer: una capacitación de crédito el lunes, una ficha clara para mandar por WhatsApp y un asesor que sí domine el tema.  
  Pantalla: Flujo: Objeción detectada → Capacitación de crédito → Ficha por WhatsApp → Más citas.

**Cierre:** Comenta INMOBILIARIO y te lo instalamos.

## S24 · «Ahorita te mando opciones»… hace dos semanas

_opciones · P12 · Junta · ~38 s · Comenta LEADS_

**Gancho en pantalla:** ¿Y LAS / [OPCIONES]?

**Personas con IA**

1. Don Ramiro lee en voz alta un mensaje en su celular, temblando de coraje; detrás de él, todos fingen trabajar.
   - **Don Ramiro:** "«Me dijeron ahorita te mando opciones… hace dos semanas.» ¡¿Quién fue?!"
   - Sonido: teclados que suenan de golpe
2. Plano general: todos señalan a Diego al mismo tiempo; Diego se esconde detrás de su laptop.
   - **Diego:** "¡Es que tenemos trescientas propiedades, jefe! No me las sé todas."
   - Sonido: whoosh de todos los brazos señalando

**Motor (narrador)**

- `chat` · El lead pidió algo clarísimo: dos recámaras, en la Roma, hasta cinco millones. Y tu asesor tardó dos semanas porque tenía que buscar a mano.  
  Pantalla: Chat de WhatsApp. Adriana Solís: «Busco depa de 2 recámaras en la Roma, hasta 5 millones». Asesor: «Ahorita te mando opciones». Hace 14 días.
- `mock` · Con Lead Master, la IA lee lo que pidió el lead y busca en tu inventario de EasyBroker las propiedades que sí coinciden.  
  Pantalla: Pantalla «Opciones para Adriana Solís»: Roma Norte, 2 rec., $4.8 M · Roma Sur, 2 rec., $4.5 M · Roma Norte, 2 rec., $4.9 M · Roma Sur, 2 rec., $4.2 M.
- `chat` · Tu asesor las revisa y se las manda en minutos, no en dos semanas. Y el cliente siente que alguien sí lo está atendiendo.  
  Pantalla: Chat: el asesor manda 3 fichas. Adriana: «¡Me gusta la segunda! ¿La puedo ver el sábado?»

**Cierre:** Comenta LEADS y te lo instalamos.

## S25 · Paola y las 40 pestañas abiertas

_opciones · P12 · Junta · ~35 s · Comenta SISTEMA_

**Gancho en pantalla:** 40 PESTAÑAS / [ABIERTAS]

**Personas con IA**

1. Primer plano de Paola frente a su laptop con decenas de pestañas abiertas; el pelo rizado cada vez más despeinado.
   - **Paola:** "Llevo una hora buscando un depa con terraza que acepte mascotas. ¡Una hora!"
   - Sonido: clics de mouse sin parar
2. Rubén se asoma por encima de sus lentes con una sonrisa orgullosa y le enseña su laptop.
   - **Rubén:** "Tranquila, yo tengo todo el inventario en un Excel."
   - **Paola:** "¿De qué año, Rubén?"
   - Sonido: Rubén carraspea; un grillo

**Motor (narrador)**

- `photo` · Tu equipo pierde horas buscando propiedades a mano entre el portal, el Excel y la memoria. Y mientras busca, el lead se enfría.  
  Pantalla: Titular: HORAS [BUSCANDO] A MANO. Foto de asesora frente a la laptop de noche.
- `mock` · En Lead Master, la IA toma lo que pidió el lead, presupuesto, zona y lo que necesita, y busca en tu inventario de EasyBroker o del portal.  
  Pantalla: Pantalla «Lo que pidió»: Del Valle · hasta $3.5 M · terraza · acepta mascotas → 3 propiedades encontradas.
- `stat` · Lo que le tomaba una hora a Paola, ahora le toma un par de minutos. Ella revisa las opciones y las manda.  
  Pantalla: Número gigante: 1 HORA → [MINUTOS].

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S26 · Plátano le mandó un penthouse de 12 millones

_opciones · P12 · Frutinovela · ~36 s · Comenta LEADS_

**Gancho en pantalla:** PIDIÓ [4] / LE MANDARON [12]

**Personas con IA**

1. Sala de juntas de frutas, música de telenovela; Don Piña sostiene un celular con la foto de un penthouse de lujo.
   - **Don Piña:** "Plátano… la señora Lucía pidió una casa de cuatro millones en Zapopan."
   - Sonido: violines que suben
2. Triple zoom dramático a Plátano Diego, que sonríe orgulloso; trueno de fondo.
   - **Don Piña:** "¡¿Y tú le mandaste un penthouse de doce millones en Polanco?!"
   - **Plátano Diego:** "Es que estaba bonito, Don Piña."
   - Sonido: trueno, golpe de orquesta

**Motor (narrador)**

- `chat` · Cuando tu asesor manda opciones que no tienen nada que ver con lo que pidió el cliente, el cliente entiende una sola cosa: no me escucharon.  
  Pantalla: Chat. Lucía Hernández: «Busco casa en Zapopan, hasta 4 millones». Asesor: ficha de penthouse en Polanco, $12 M. Lucía: «Ok… gracias». Visto.
- `mock` · Lead Master lee lo que pidió el lead y busca en tu inventario opciones que sí coinciden en presupuesto y en zona.  
  Pantalla: Pantalla «Lucía Hernández · Zapopan · hasta $4 M» → 3 casas: $3.6 M, $3.9 M, $4 M.
- `compare` · Tu asesor manda lo que el cliente sí puede comprar, en minutos. Y nadie vuelve a mandar un penthouse porque estaba bonito.  
  Pantalla: Antes: penthouse de $12 M «porque estaba bonito». Con Lead Master: 3 casas en Zapopan hasta $4 M.

**Cierre:** Comenta LEADS y te lo instalamos.

## S27 · «Tres días… pero eran muy buenas»

_opciones · P12 · Junta · ~35 s · Comenta LEADS_

**Gancho en pantalla:** ¿CUÁNTO / [TARDASTE]?

**Personas con IA**

1. Andrés entra a la sala de juntas mirando su celular escondido debajo de la chamarra; Don Ramiro lo detiene con la mirada.
   - **Andrés:** "Jefe, el cliente del depa de Polanco ya compró con otra inmobiliaria."
   - Sonido: puerta que se cierra, silencio
2. Don Ramiro se inclina hacia Andrés con una calma que da miedo; Andrés traga saliva.
   - **Don Ramiro:** "¿Cuánto tardaste en mandarle opciones?"
   - **Andrés:** "Tres días… pero eran muy buenas."
   - Sonido: un tic de reloj, tensión

**Motor (narrador)**

- `events` · Lunes, el lead pide opciones. Martes, otra inmobiliaria le manda tres. Miércoles, las visita. Jueves, por fin le llegan las tuyas.  
  Pantalla: Línea de tiempo: Lun 10:12 pide opciones · Mar 9:40 la competencia le manda 3 · Mié 17:00 visita · Jue 18:05 llegan las tuyas.
- `mock` · Con Lead Master, en cuanto el lead pide algo, la IA busca en tu inventario de EasyBroker y le deja las opciones listas a tu asesor.  
  Pantalla: Pantalla: nuevo mensaje del lead → «Opciones encontradas: 4» → botón «Revisar y enviar».
- `compare` · En bienes raíces, el que contesta primero con buenas opciones se queda con la visita. Con Lead Master, ese puede ser tu equipo todos los días.  
  Pantalla: Antes: 3 días. Con Lead Master: [MINUTOS].

**Cierre:** Comenta LEADS y te lo instalamos.

## S28 · ¿Teníamos casa con alberca o no teníamos?

_opciones · P12 · Junta · ~37 s · Comenta INMOBILIARIO_

**Gancho en pantalla:** ¿TENÍAMOS / [ESA] CASA?

**Personas con IA**

1. Don Ramiro con el puño sobre la mesa y la vena de la frente saltando; todos lo miran sin parpadear.
   - **Don Ramiro:** "El cliente quería casa con alberca en Juriquilla. ¿Teníamos o no teníamos?"
   - Sonido: puño en la mesa
2. Paola y Diego se miran; Paola levanta tres dedos, a Diego se le abren los ojos como platos.
   - **Paola:** "Teníamos tres."
   - **Diego:** "¿¡Tres!? Yo le dije que no había nada…"
   - Sonido: golpe de música de suspenso

**Motor (narrador)**

- `photo` · Tu equipo no se sabe todo tu inventario de memoria. Nadie se lo sabe. Y por eso a veces dicen que no hay, cuando sí hay.  
  Pantalla: Titular: SÍ HABÍA. NADIE [SABÍA]. Foto de casa con alberca.
- `mock` · Lead Master toma lo que el lead pidió en el chat y busca en tu inventario de EasyBroker o del portal lo que coincide, aunque el asesor no se acuerde.  
  Pantalla: Pantalla «Juriquilla · casa · con alberca» → 3 propiedades de tu inventario.
- `chat` · Tu asesor revisa, manda las tres y agenda la visita. Esa venta ya no se va con la competencia por no saber lo que tenías.  
  Pantalla: Chat: el asesor manda 3 fichas. Lead: «¡La segunda! ¿El sábado a las 11?» Inserto de cita agendada: sábado 11:00.

**Cierre:** Comenta INMOBILIARIO y te lo instalamos.

## S29 · La contraseña del portal la tenía la practicante

_portales · P11 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** ¿QUIÉN REVISÓ / EL [PORTAL]?

**Personas con IA**

1. Don Ramiro señala la pantalla de la sala, donde se ve una bandeja de mensajes con un número rojo enorme sin leer.
   - **Don Ramiro:** "¿Quién revisó los leads de Inmuebles24 esta semana? ¿Nadie?"
   - Sonido: zumbido de proyector
2. Rubén sube la mano despacio, sin despegar los ojos de su Excel; Don Ramiro se acerca.
   - **Rubén:** "La contraseña la tenía la practicante, jefe."
   - **Don Ramiro:** "¿Y la practicante?!"
   - Sonido: Rubén contesta bajito: «se fue en agosto»; un grillo

**Motor (narrador)**

- `stat` · Cuando un portal depende de que alguien entre a revisar, pasa esto: cuarenta y seis leads sin abrir. Personas que preguntaron por una propiedad y nadie les contestó.  
  Pantalla: Número gigante: [46] leads sin abrir · Inmuebles24 · últimas 3 semanas.
- `flow` · Lead Master está conectado a tus portales, EasyBroker, Inmuebles24 y otros. Cada lead entra solo al sistema y se le asigna a un asesor.  
  Pantalla: Flujo: Portal → Lead Master → Asignado a Paola G. → Llamada.
- `phonelist` · Y si ese asesor no lo atiende a tiempo, pasa al siguiente. Nadie tiene que entrar al portal. Ni acordarse de la contraseña.  
  Pantalla: Celular de Paola: «Nuevo lead de Inmuebles24: Diana Trejo · asignado a ti».

**Cierre:** Comenta LEADS y te lo instalamos.

## S30 · El lead del viernes a las 9 de la noche

_portales · P11 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** VIERNES, / [9:00] PM

**Personas con IA**

1. Lunes temprano; Don Ramiro con un café en la mano y cara de pocos amigos lee una notificación en su celular.
   - **Don Ramiro:** "Un lead de EasyBroker pidió visita el viernes a las nueve. ¿Quién lo vio?"
   - Sonido: sorbo de café, taza que se azota
2. Diego bosteza con lentes de sol puestos; Paola lo mira de reojo.
   - **Diego:** "Lo vi hoy, jefe… pero ya se fue a ver otro desarrollo."
   - **Paola:** "Los portales no descansan, Diego."
   - Sonido: bostezo largo, golpe de música

**Motor (narrador)**

- `events` · Viernes, nueve de la noche: el lead pide visita. Sábado: otra inmobiliaria le contesta. Lunes: tu equipo por fin abre el portal.  
  Pantalla: Línea de tiempo: Vie 21:04 lead de EasyBroker · Sáb 10:15 la competencia contesta · Lun 9:30 tu equipo lo ve.
- `flow` · Con Lead Master, el lead del portal entra solo al sistema en cuanto llega y se le asigna a un asesor. No espera a que alguien revise el lunes.  
  Pantalla: Flujo: EasyBroker (vie 21:04) → Lead Master → Asignado a Paola G. (21:04).
- `phonelist` · Si el asesor no lo atiende a tiempo, pasa al siguiente. Y el sábado en la mañana ese lead ya está en la lista de urgentes.  
  Pantalla: Celular, «Tu lista de hoy · sábado 8:00 am»: Urgentes (2) · Diana Trejo: pidió visita ayer a las 21:04.

**Cierre:** Comenta LEADS y te lo instalamos.

## S31 · El portal que nadie abre (y la contraseña perdida)

_portales · P11 · Junta · ~37 s · Comenta LEADS_

**Gancho en pantalla:** 46 LEADS / SIN [ABRIR]

**Personas con IA**

1. Plano medio en la sala de juntas: Don Ramiro, rojo, señala una laptop cerrada en la mesa; Diego se encoge en su silla con el saco grande.
   - **Don Ramiro:** "¿Quién tiene la contraseña del portal? ¡Llevo dos semanas sin ver un solo lead!"
   - **Diego:** "La cambié yo, jefe… y no me acuerdo cuál puse."
   - Sonido: silencio incómodo, un reloj de pared
2. Rubén, con los lentes en la punta de la nariz, voltea la laptop hacia la mesa; la bandeja del portal llena de mensajes sin abrir. Don Ramiro abre los ojos enormes.
   - **Rubén:** "Ya entré. Hay cuarenta y seis leads sin abrir. Desde octubre."
   - **Don Ramiro:** "¡¿Desde octubre?!"
   - Sonido: golpe dramático, tazas que tiemblan

**Motor (narrador)**

- `photo` · Si para ver tus leads de portales alguien tiene que entrar a revisar, se te pierden. El lead que espera tres días ya le escribió a otra inmobiliaria.  
  Pantalla: Titular: 46 LEADS SIN [ABRIR]. Foto de laptop con una bandeja de entrada llena.
- `flow` · Lead Master está conectado a EasyBroker, Inmuebles24 y otros portales. Cada vez que alguien deja sus datos, el lead aparece solo en el sistema.  
  Pantalla: Flujo: EasyBroker / Inmuebles24 / otros portales → Lead Master → asesor.
- `ui+crm` · Se asigna a un asesor en ese momento y, si no lo atiende a tiempo, pasa al siguiente. Nadie tiene que entrar al portal a revisar nada.  
  Pantalla: Tarjeta: Adriana Solís · Inmuebles24 · Depa 2 recámaras · asignada a Paola G. Contador de 10 min; al llegar a cero pasa a Valeria R.

**Cierre:** Comenta LEADS y te mostramos cómo se conecta tu portal.

## S32 · Llegó el viernes a las 9 pm. Lo vio el miércoles

_portales · P11 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** LLEGÓ EL VIERNES / LO VIO [HOY]

**Personas con IA**

1. Plano medio: Diego, sonriente, levanta su celular como si trajera buenas noticias; Don Ramiro, al lado, deja de tomar café a medio sorbo.
   - **Diego:** "Jefe, entró un lead buenísimo del portal. Llegó el viernes en la noche, lo vi hoy."
   - **Don Ramiro:** "¡¿Hoy?! ¡Diego, es miércoles!"
   - Sonido: café que se derrama, golpe de taza
2. Paola, sin levantar la vista de su laptop, con sarcasmo; Diego se queda congelado con el celular en alto.
   - **Paola:** "Ya compró. Con la inmobiliaria de enfrente. Me la encontré en la tiendita."
   - Sonido: grillos

**Motor (narrador)**

- `events` · Viernes, nueve de la noche: un lead pregunta por una casa de seis millones en un portal. Sábado: otra inmobiliaria le contesta. Miércoles: tu asesor lo ve.  
  Pantalla: Línea de tiempo: Vie 9:04 pm lead nuevo · Sáb 10:12 am le contesta la competencia · Mié 11:30 am Diego abre el portal.
- `ui+crm` · Con Lead Master, el lead del portal entra al sistema al instante y se asigna a un asesor, aunque sea viernes en la noche.  
  Pantalla: Notificación 9:04 pm: Nuevo lead · Inmuebles24 · Lucía Hernández · asignado a Paola G.
- `phonelist` · Si no lo atiende a tiempo, pasa al siguiente. Y a las ocho de la mañana ya está en la lista de urgentes de tu asesor.  
  Pantalla: Lista del día 8:00 am · Lo urgente: Lucía Hernández (portal, viernes 9:04 pm).

**Cierre:** Comenta LEADS y te lo instalamos.

## S33 · 40 mil pesos al mes por un logo verde

_portales · P11 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** ¿CUÁL PORTAL / TE [VENDE]?

**Personas con IA**

1. Sala de juntas: Don Ramiro con tres facturas en la mano; Karla, con su tablet, sonríe forzada.
   - **Don Ramiro:** "Pagamos tres portales. Tres. ¿Cuál nos vende? ¡Uno! ¡Díganme uno!"
   - **Karla:** "¡Todos traen leads, Don Ramiro! ¡Muchísimos!"
   - Sonido: papeles golpeando la mesa
2. Rubén revisa su Excel enorme, entrecierra los ojos; Don Ramiro se tapa la cara con las dos manos.
   - **Rubén:** "Según mi Excel, el que más vende es… ¿el del logo verde?"
   - **Don Ramiro:** "¡Estoy pagando cuarenta mil pesos al mes por un logo verde!"
   - Sonido: suspiro largo, tecla de computadora

**Motor (narrador)**

- `photo` · Muchas inmobiliarias pagan dos o tres portales cada mes y nadie sabe cuál trae compradores y cuál trae puros curiosos. Se renueva todo por costumbre.  
  Pantalla: Titular: ¿CUÁL PORTAL TE [VENDE]? Foto de facturas sobre un escritorio.
- `flow` · Lead Master recibe los leads de todos tus portales en un solo lugar y sabe de dónde vino cada uno.  
  Pantalla: Flujo: EasyBroker, Inmuebles24 y otro portal → Lead Master, cada lead con su etiqueta de origen.
- `bars` · Así ves, portal por portal, cuántos leads llegaron, a cuántos se les llamó y cuántas citas salieron. Y decides dónde poner tu dinero con datos, no con corazonadas.  
  Pantalla: Barras por portal (ejemplo): Portal A 120 leads · 14 citas · Portal B 85 leads · 3 citas · Portal C 40 leads · 9 citas.

**Cierre:** Comenta LEADS y te enseñamos tus números por portal.

## S34 · Diego descartó 37 leads en una semana

_anecdotas · P06 · Junta · ~38 s · Comenta LEADS_

**Gancho en pantalla:** 37 LEADS / [DESCARTADOS]

**Personas con IA**

1. Don Ramiro lee una hoja larguísima que se desenrolla hasta el piso; Diego se ajusta los lentes, nervioso.
   - **Don Ramiro:** "Diego, descartaste treinta y siete leads esta semana. ¿Todos dicen «no contesta»?"
   - **Diego:** "Es que la gente ya no contesta, jefe. Es la economía."
   - Sonido: papel desenrollándose
2. Paola levanta su celular con una sonrisa triunfal; Diego traga saliva en primer plano.
   - **Paola:** "Yo le marqué a tres de tus descartados. Uno ya agendó para el sábado."
   - Sonido: ding de notificación, golpe dramático

**Motor (narrador)**

- `stat` · Pasó en una inmobiliaria: un asesor descartó treinta y siete leads en una semana. A treinta y uno les marcó una sola vez, todos entre la una y las tres de la tarde.  
  Pantalla: Número gigante: 37 DESCARTADOS. Abajo: 31 con un solo intento.
- `ui+crm` · En Lead Master ves cada lead que tu asesor descartó, con el motivo, cuántas veces le marcó y la conversación completa.  
  Pantalla: Lista de descartados: Diego H. · 37 · motivo «no contesta» · intentos: 1 · ver conversación.
- `compare` · Si el descarte no tiene sentido, se lo pasas a otro asesor. En ese caso, otra asesora retomó los treinta y siete: contestaron catorce y agendaron tres.  
  Pantalla: Antes: 37 descartados. Después de reasignar: 14 contestaron · 3 citas.

**Cierre:** Comenta LEADS y revisa tus descartados.

## S35 · ¿Qué primo, Andrés?

_anecdotas · P04 · Junta · ~38 s · Comenta LEADS_

**Gancho en pantalla:** ¿QUÉ [PRIMO], / ANDRÉS?

**Personas con IA**

1. Andrés, en una esquina de la sala con la chamarra de cuero, susurra al celular tapándose la boca; Don Ramiro aparece justo detrás de él, con los brazos cruzados.
   - **Andrés:** "Sí, primo, te paso al cliente por fuera… le sale más barato."
   - **Don Ramiro:** "¿Qué primo, Andrés?"
   - Sonido: golpe musical seco
2. Andrés guarda el celular de golpe y sonríe nervioso; Paola, desde la mesa, levanta una ceja.
   - **Andrés:** "Mi primo… el que vende tacos."
   - **Paola:** "Tacos de departamentos de cuatro millones."
   - Sonido: grillos

**Motor (narrador)**

- `photo` · Pasó en una inmobiliaria: un asesor cerraba poco, pero sus leads siempre se enfriaban. Tres de ellos compraron en un mes con la inmobiliaria de su primo.  
  Pantalla: Titular: SUS LEADS SE [ENFRIABAN]. Foto de asesor con el celular escondido.
- `chat` · Mientras el lead viva en el WhatsApp personal de tu asesor, no ves qué le dicen ni a quién se lo pasan.  
  Pantalla: Chat: Andrés M.: «Te paso con un socio, por fuera te sale mejor la comisión». Diana Trejo: «Va, pásame su número».
- `stack` · Con Lead Master, el WhatsApp de cada asesor está conectado, solo las conversaciones con leads. Las llamadas salen del sistema y quedan grabadas. Y si pasa algo raro con un lead, te llega un aviso.  
  Pantalla: Tarjetas: WhatsApp conectado (solo leads) · Llamadas grabadas · Aviso: algo raro con Diana Trejo (Andrés M.).

**Cierre:** Comenta LEADS y cierra la puerta.

## S36 · Aguacate renuncia y se lleva los leads

_anecdotas · P04 · Frutinovela · ~39 s · Comenta LEADS_

**Gancho en pantalla:** SE FUE CON / [120] LEADS

**Personas con IA**

1. Sala de juntas de frutas, música de telenovela: Aguacate Andrés entra con una caja de cartón con sus cosas; Don Piña, en la cabecera, aprieta la corona de hojas.
   - **Aguacate Andrés:** "Don Piña, renuncio. Me voy a otra inmobiliaria."
   - **Don Piña:** "Está bien, Aguacate… pero mis leads se quedan."
   - Sonido: violines dramáticos
2. Aguacate sonríe de lado y agita su celular; triple zoom a la cara de Don Piña, que cae de rodillas mientras Fresa Valeria se tapa la boca.
   - **Aguacate Andrés:** "¿Cuáles leads? Los ciento veinte están en mi celular."
   - **Don Piña:** "¡Aguacateeee!"
   - Sonido: trueno, golpe de telenovela

**Motor (narrador)**

- `stat` · Pasó en una inmobiliaria: un asesor con ciento veinte leads activos renunció un viernes. El lunes no había nada: los chats estaban en su celular y las notas en su libreta.  
  Pantalla: Número gigante: 120 LEADS SE FUERON.
- `events` · Dos de esos leads compraron con él en su nueva inmobiliaria. Y nadie pudo hacer nada, porque no había historial.  
  Pantalla: Línea de tiempo: Viernes renuncia · Lunes: 0 historial · Mes siguiente: 2 ventas con la competencia.
- `ui+crm` · En Lead Master el historial es de tu inmobiliaria: cada chat, cada llamada grabada y cada nota se quedan aunque el asesor se vaya. El que sigue retoma cada lead con todo el contexto.  
  Pantalla: Ficha: Andrés M. dejó la empresa · 120 leads · historial completo (chats, llamadas, notas) · asignar a Paola G. y Valeria R.

**Cierre:** Comenta LEADS antes de que se te vaya el siguiente.

## S37 · 22 leads calientitos… de hace tres semanas

_anecdotas · P05 · Junta · ~35 s · Comenta SISTEMA_

**Gancho en pantalla:** 22 LEADS / [CALIENTITOS]

**Personas con IA**

1. Plano medio: Don Ramiro con los brazos cruzados; Diego, muy confiado, se recarga en la silla con las manos detrás de la cabeza.
   - **Don Ramiro:** "Diego, ¿cuántos leads nuevos tienes?"
   - **Diego:** "Veintidós, jefe. Todos calientitos."
   - Sonido: murmullo de oficina
2. Don Ramiro se inclina sobre la mesa; Diego pierde la sonrisa y la silla se le va para atrás. Rubén escupe el café.
   - **Don Ramiro:** "¿Y a cuántos les has hablado?"
   - **Diego:** "¿Hoy… o en general?"
   - Sonido: silla cayendo, café escupido

**Motor (narrador)**

- `stat` · En muchas inmobiliarias, uno de cada tres leads nunca habló con nadie. No es que no contestaran: nadie les marcó.  
  Pantalla: Número gigante: 1 DE CADA 3 NUNCA HABLÓ CON NADIE.
- `phonelist` · Con Lead Master, cada asesor recibe a las ocho de la mañana su lista del día: lo urgente, los que nunca ha buscado y los que se están enfriando.  
  Pantalla: Lista del día de Diego H.: Lo urgente 3 · Nunca los has buscado 22 · Se están enfriando 5.
- `ui+report` · Y tú recibes el reporte: cuántos leads entraron, a quién llamó cada asesor y quién se quedó sin contacto. Con nombre y apellido.  
  Pantalla: Reporte del equipo: Paola G. llamó a 14 · Diego H. llamó a 0 · Sin contacto: 22 (Diego H.).

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S38 · «No me haga perder el tiempo»: la captura viral

_anecdotas · P07 · Junta · ~37 s · Comenta SISTEMA_

**Gancho en pantalla:** ¿QUIÉN ESCRIBIÓ / [ESTO]?

**Personas con IA**

1. Don Ramiro lee su celular en voz alta, incrédulo; todos alrededor de la mesa se voltean a ver a Andrés.
   - **Don Ramiro:** "«Si no tiene para el enganche, no me haga perder el tiempo». ¿Quién escribió esto?"
   - **Andrés:** "Pues… era la verdad, jefe."
   - Sonido: golpe dramático
2. Karla entra corriendo con su tablet en alto; Don Ramiro se deja caer en la silla con la cara entre las manos.
   - **Karla:** "Ya está en el grupo de Facebook de la colonia. Tiene trescientos comentarios."
   - Sonido: notificaciones sonando sin parar

**Motor (narrador)**

- `chat` · Pasó en una inmobiliaria: un lead preguntó si podía comprar con crédito y el asesor le contestó esto. El lead publicó la captura y el dueño se enteró por un comentario.  
  Pantalla: Chat: Lucía Hernández: «¿Aceptan crédito?» · Asesor: «Si no tiene para el enganche no me haga perder el tiempo».
- `photo` · Lo que escribe tu asesor lo firma tu inmobiliaria. Y casi siempre te enteras cuando ya es público.  
  Pantalla: Titular: LO QUE ESCRIBE TU ASESOR LO [FIRMAS] TÚ.
- `stack` · Con Lead Master, las conversaciones con leads viven en tu sistema: las lees sin pedirle el celular a nadie, y te llega un aviso cuando pasa algo raro con un lead.  
  Pantalla: Tarjetas: Conversaciones con leads en tu sistema · Llamadas grabadas · Aviso: conversación a revisar (Lucía Hernández).

**Cierre:** Comenta SISTEMA y entérate antes que Facebook.

## S39 · 90 % contactados, según el Excel

_anecdotas · P13 · Junta · ~37 s · Comenta SISTEMA_

**Gancho en pantalla:** 90 % SEGÚN / EL [EXCEL]

**Personas con IA**

1. Rubén presenta orgulloso en la pantalla de la sala un Excel con un 90 % gigante en verde; Don Ramiro lo mira con los ojos entrecerrados.
   - **Rubén:** "¡Noventa por ciento de leads contactados, Don Ramiro! ¡Récord!"
   - **Don Ramiro:** "¿Noventa? ¿Y por qué este mes vendimos tres?"
   - Sonido: fanfarria que se corta de golpe
2. Al fondo de la mesa, Diego se acerca a Paola y le susurra tapándose la boca; los dos miran al techo.
   - **Diego:** "Yo puse que llamé a todos… por si acaso."
   - **Paola:** "Yo también."
   - Sonido: silbido inocente

**Motor (narrador)**

- `compare` · Pasó en una inmobiliaria: el Excel decía noventa por ciento de leads contactados. Cuando conectaron los WhatsApp y las llamadas, el número real fue cuarenta y uno.  
  Pantalla: Comparación: Según el Excel 90 % · Según los chats y las llamadas 41 %.
- `photo` · Nadie mentía a propósito. Cada asesor llenaba lo que se acordaba. Un reporte que alguien llena a mano es una opinión.  
  Pantalla: Titular: UN REPORTE A MANO ES UNA [OPINIÓN]. Foto de Excel de noche.
- `ui+report` · Lead Master arma el reporte solo, con lo que de verdad pasó en los chats y las llamadas. Te llega todos los días a tu WhatsApp, sin que nadie llene nada.  
  Pantalla: Reporte del equipo: Leads que entraron 37 · Contactados 15 (41 %) · Sin contacto 22 · Citas 3.

**Cierre:** Comenta SISTEMA y recibe el reporte de verdad.

## S40 · Plátano Diego y las 15 llamadas en 3 minutos

_anecdotas · P05 · Frutinovela · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** 15 LLAMADAS / EN [3] MINUTOS

**Personas con IA**

1. Sala de juntas de frutas, música de telenovela: Don Piña de brazos cruzados frente a Plátano Diego, que levanta la mano como jurando.
   - **Don Piña:** "Plátano Diego, ¿le marcaste a Lucía Hernández?"
   - **Plátano Diego:** "¡Quince veces, Don Piña! ¡Lo juro por mi racimo!"
   - Sonido: violines de suspenso
2. Limón abre la laptop con triple zoom dramático; Plátano Diego se pone café de los nervios y Don Piña se levanta furioso.
   - **Limón:** "Quince llamadas… en tres minutos. A las dos de la tarde. En plena comida."
   - **Don Piña:** "¡Plátanooo!"
   - Sonido: trueno, golpe de telenovela

**Motor (narrador)**

- `events` · Quince intentos en tres minutos no son seguimiento. Son un solo intento, justo a la hora en que nadie contesta.  
  Pantalla: Registro de llamadas: Diego H. → Lucía Hernández · 15 llamadas entre 2:47 y 2:50 pm · 0 contestadas.
- `bars` · Lead Master registra cada llamada que sale del sistema: cuántos intentos, a qué hora y cuánto duró. Y te dice a qué hora sí te contestan tus leads.  
  Pantalla: Barras de tasa de contestación por horario (ejemplo): 2 pm 8 % · 11 am 21 % · 7 pm 38 %.
- `phonelist` · Así tu asesor sabe a quién volver a llamar cada día, tú ves cada intento real, y dejas de escuchar «le marqué quince veces» en la junta.  
  Pantalla: Lista del día de Diego H.: No te han contestado · Lucía Hernández (2.º intento).

**Cierre:** Comenta SISTEMA y te lo instalamos.

## S41 · 412 descartados y nadie sabe por qué

_descartados · P06 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** 412 LEADS / [DESCARTADOS]

**Personas con IA**

1. Plano medio de Don Ramiro en la cabecera de la mesa; desenrolla una hoja impresa tan larga que cae de la mesa y rueda por el piso de la sala de juntas.
   - **Don Ramiro:** "¿Cuatrocientos doce descartados? ¡¿Quién descartó a media ciudad?!"
   - Sonido: papel desenrollándose, rollo que cae al piso
2. Contraplano: Diego encogido detrás de su laptop, sudando; a su lado Paola cruza los brazos y lo mira de reojo.
   - **Diego:** "Jefe, es que no contestaban…"
   - **Paola:** "Les marcó una vez. A la hora de la comida."
   - Sonido: silencio incómodo, un grillo

**Motor (narrador)**

- `photo` · En casi todas las inmobiliarias, descartar un lead es un clic. Y nadie revisa por qué se descartó.  
  Pantalla: Titular: UN CLIC Y [ADIÓS]. Foto de asesor frente a la laptop.
- `mock` · En Lead Master ves cada lead descartado, quién lo descartó, el motivo y la conversación completa. Así sabes si de verdad no le interesaba o si nadie le insistió.  
  Pantalla: Pantalla de descartados: Diego H. · 37 descartados esta semana · motivo «no contesta» · 31 con un solo intento.
- `ui+crm` · Y si estaba mal descartado, lo reasignas a otro asesor antes de que compre con la competencia. Ese lead ya lo pagaste en anuncios.  
  Pantalla: Tarjeta de Lucía Hernández pasa de «Descartado» a «Paola G. · llamar hoy».

**Cierre:** Comenta LEADS y te enseñamos tus descartados.

## S42 · Motivo de descarte: «no le interesa»

_descartados · P06 · Junta · ~35 s · Comenta LEADS_

**Gancho en pantalla:** NO LE INTERESA / ¿[SEGURO]?

**Personas con IA**

1. Plano medio de Don Ramiro con los lentes en la mano, leyendo la pantalla de la laptop en voz alta; la vena de la frente le empieza a latir.
   - **Don Ramiro:** "Motivo de descarte: «no le interesa». Diego… ¡el señor preguntó por el enganche!"
   - Sonido: tic del reloj de la sala
2. Diego se acomoda el saco que le queda grande, muy seguro de sí; al fondo Rubén se baja los lentes y se tapa la cara con la mano.
   - **Diego:** "Bueno, jefe, preguntar no es comprar."
   - Sonido: palmada en la frente

**Motor (narrador)**

- `chat` · Este es el chat del lead que Diego descartó por «no le interesa». Preguntó por el enganche, le dijeron «le paso info» y nadie volvió a escribirle.  
  Pantalla: Chat: Lead: «¿De cuánto es el enganche del depa de 2 recámaras?» · Diego: «le paso info» · tres días sin mensajes · etiqueta roja: Descartado, no le interesa.
- `mock` · Lead Master pone al lado de cada motivo la conversación completa. Si el lead preguntó por el enganche, por el crédito o por una visita, no era un curioso.  
  Pantalla: Descartado · Motivo: «no le interesa» · Última pregunta del lead: «¿de cuánto es el enganche?» · botón Revisar.
- `ui+crm` · Lo reasignas y otro asesor le llama hoy. Ya pagaste por ese lead. Que no se pierda por un clic.  
  Pantalla: Reasignado a Paola G. · llamada hoy 5:00 pm.

**Cierre:** Comenta LEADS y revisamos tus descartados.

## S43 · La «curiosa» ya subió foto con las llaves

_descartados · P06 · Junta · ~37 s · Comenta INMOBILIARIO_

**Gancho en pantalla:** YA COMPRÓ. / [CON OTRO]

**Personas con IA**

1. Paola le enseña su celular a Don Ramiro: en la pantalla, una foto de una señora sonriendo con unas llaves frente a una casa nueva. Don Ramiro sonríe orgulloso.
   - **Paola:** "Jefe, ¿se acuerda de Adriana Solís? Ya compró. Subió foto con las llaves."
   - **Don Ramiro:** "¡Qué bien! ¿Quién se la cerró?"
   - Sonido: murmullo de oficina
2. Silencio. Paola niega lentamente con la cabeza. Don Ramiro se pone rojo de abajo hacia arriba como termómetro y le sale vapor de las orejas; Diego se desliza debajo de la mesa.
   - **Paola:** "Nosotros no, jefe."
   - Sonido: silbido de olla exprés

**Motor (narrador)**

- `events` · Adriana dejó sus datos en marzo. Diego le marcó una vez, la puso como curiosa y nadie más la buscó. En mayo compró una casa de 4 millones con otra inmobiliaria.  
  Pantalla: Línea de tiempo: 3 mar entra el lead · 3 mar 1 llamada · 4 mar descartada «curiosa» · 12 may compró con otra inmobiliaria.
- `stat` · Una casa de 4 millones al 3 por ciento son 120 mil pesos de comisión que se fueron por un clic.  
  Pantalla: Número gigante: $120,000 · comisión que se fue.
- `mock` · En Lead Master revisas los descartados de la semana con su motivo y su conversación, y reasignas los que todavía se pueden rescatar.  
  Pantalla: Descartados esta semana: 23 · Por revisar: 9 · Reasignados: 4.

**Cierre:** Comenta INMOBILIARIO y te enseñamos cómo.

## S44 · La caja que el Plátano escondía

_descartados · P06 · Frutinovela · ~38 s · Comenta LEADS_

**Gancho en pantalla:** LA CAJA DE LOS / [DESCARTADOS]

**Personas con IA**

1. Sala de juntas de frutas. Fresa Valeria saca de debajo del escritorio de Plátano Diego una caja empolvada que dice DESCARTADOS; la abre y se ilumina como un tesoro. Zoom lento, música de telenovela.
   - **Fresa Valeria:** "Don Piña… aquí hay ciento cincuenta leads… ¡y todos siguen vivos!"
   - Sonido: coro dramático
2. Don Piña con la corona de hojas erizada encara a Plátano Diego, que se pone café de los nervios. Trueno, triple zoom a la cara del Plátano.
   - **Don Piña:** "¡Plátano! ¿Por qué escondiste estos leads?"
   - **Plátano Diego:** "No los escondí… ¡los descarté!"
   - Sonido: trueno, golpe de piano

**Motor (narrador)**

- `photo` · En muchas inmobiliarias «descartado» quiere decir «nadie lo vuelve a ver». Y ahí hay leads que sí iban a comprar.  
  Pantalla: Titular: LEADS [ENTERRADOS]. Foto de oficina vacía de noche.
- `mock` · Lead Master te muestra cada descartado con el motivo, cuántas veces se le llamó y la última conversación. Si a un lead se le marcó una sola vez, lo ves.  
  Pantalla: Tabla: Diego H. · 150 descartados · 112 con un solo intento · motivo más común: «no contesta».
- `ui+call` · Y los rescatas: los reasignas o los llamas uno tras otro con un botón. Si alguien contesta, hablas, y lo que se dijo queda en notas.  
  Pantalla: Botón «Llamar a todos (38)» · llamada en curso a Lucía Hernández · nota que se escribe sola.

**Cierre:** Comenta LEADS y rescatamos tu caja de descartados.

## S45 · El viernes de revisar descartados a mano

_descartados · P06 · Junta · ~35 s · Comenta SISTEMA_

**Gancho en pantalla:** 600 CHATS / A [MANO]

**Personas con IA**

1. Don Ramiro de pie con una lupa gigante en la mano, como detective; los cuatro asesores alrededor de la mesa abren la boca horrorizados.
   - **Don Ramiro:** "¡A partir de hoy, cada viernes revisamos uno por uno los leads que descartaron!"
   - Sonido: golpe de orquesta de suspenso
2. Rubén gira su laptop: una lista que no se acaba. Don Ramiro baja la lupa despacio y se sienta derrotado.
   - **Rubén:** "Jefe, son seiscientos. Nos quedamos hasta el lunes."
   - Sonido: trombón triste

**Motor (narrador)**

- `photo` · Revisar descartados a mano no escala. Nadie tiene tiempo de leer seiscientos chats un viernes en la tarde. Y si nadie los revisa, tus asesores aprenden que descartar no tiene consecuencias.  
  Pantalla: Titular: 600 CHATS [A MANO]. Foto de Excel de noche.
- `mock` · Lead Master te los ordena: cada descartado con su asesor, su motivo, cuántas veces se le llamó y la conversación al lado.  
  Pantalla: Descartados agrupados por asesor y por motivo, con número de intentos y botón Ver conversación.
- `bars` · Así ves en cinco minutos que Diego descarta cuatro veces más que Paola, y casi siempre con una sola llamada.  
  Pantalla: Barras de descartados del mes: Diego H. 37 · Andrés M. 21 · Valeria R. 9 · Paola G. 8 · etiqueta «con 1 solo intento».

**Cierre:** Comenta SISTEMA y te lo enseñamos con tus datos.

## S46 · Karla trajo un bot que atiende solito

_circulos · P01 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** PRESIONE 1 / PARA [VENDER]

**Personas con IA**

1. Karla, con blazer morado, presenta su tablet frente a la mesa con sonrisa forzada de comercial; Don Ramiro la escucha con los brazos cruzados.
   - **Karla:** "¡Les traje un bot que atiende solito a sus clientes, veinticuatro siete!"
   - **Don Ramiro:** "¿Y vende?"
   - Sonido: fanfarria de anuncio
2. Paola lee en voz alta desde su celular, sin emoción; todos voltean despacio a ver a Karla, que mantiene la sonrisa congelada.
   - **Paola:** "Un cliente preguntó por un depa en Polanco. El bot le contestó: «presione uno»."
   - Sonido: disco rayado

**Motor (narrador)**

- `chat` · Así atienden muchos bots a alguien que quiere comprar un departamento de 6 millones. El cliente pregunta algo concreto y el bot lo manda a dar vueltas en un menú.  
  Pantalla: Chat: Lead: «¿El depa de Polanco tiene estacionamiento?» · Bot: «Presione 1 para ventas, 2 para rentas» · Lead: «?» · Bot: «No entendí. Presione 1» · el lead deja de contestar.
- `photo` · Nadie compra una casa porque un bot le contestó rápido. La compra porque una persona le dio seguimiento.  
  Pantalla: Titular: COMPRA POR UNA [PERSONA]. Foto de recorrido con asesora.
- `phonelist` · En Lead Master la IA trabaja para tu asesor: lee los chats y las llamadas, llena el CRM y cada mañana le dice a quién llamar.  
  Pantalla: Lista del día por WhatsApp: Lo urgente 3 · Nunca los has buscado 5 · No te contestaron 7 · Se están enfriando 4.

**Cierre:** Comenta SISTEMA. Y no, no despide a nadie.

## S47 · Karla vs. Diego: primer round

_circulos · P02 · Junta · ~36 s · Comenta LEADS_

**Gancho en pantalla:** MARKETING / VS. [VENTAS]

**Personas con IA**

1. Karla y Diego frente a frente en la sala de juntas como boxeadores; Don Ramiro en medio hace de réferi y toca una campanita.
   - **Don Ramiro:** "¡Primer round! La agencia dice que los leads son buenos. Ventas dice que son basura."
   - Sonido: campana de box, multitud
2. Karla y Diego se gritan a la cara; Paola levanta la mano desde su silla sin despegar los ojos de su café.
   - **Karla:** "¡Les mando trescientos a la semana!"
   - **Diego:** "¡Y ninguno contesta!"
   - **Paola:** "Diego, les marcas a los tres días."
   - Sonido: golpe de K.O.

**Motor (narrador)**

- `photo` · Esta pelea pasa en casi todas las inmobiliarias, y siempre gana el que grita más fuerte, porque nadie tiene los datos.  
  Pantalla: Titular: GANA EL QUE [GRITA]. Foto de marketing y ventas peleando.
- `bars` · Lead Master te dice por campaña cuántos leads entraron, en cuánto tiempo se les llamó y cuántos agendaron cita. Así sabes si el problema es la campaña o el seguimiento.  
  Pantalla: Barras por campaña: Campaña A · 120 leads · llamados en 18 min · 14 citas | Campaña B · 180 leads · llamados en 2 días · 3 citas.
- `flow` · Y le avisa a Meta quién sí agenda y compra, para que te traiga más compradores y menos curiosos. Se acabó la pelea.  
  Pantalla: Flechas: El lead agenda → Lead Master avisa a Meta → Meta busca más gente como esa.

**Cierre:** Comenta LEADS y ponemos los datos en la mesa.

## S48 · Rubén proyecta el CRM: 300 leads en «Nuevo»

_circulos · P03 · Junta · ~35 s · Comenta CRM_

**Gancho en pantalla:** 300 LEADS EN / [NUEVO]

**Personas con IA**

1. Rubén proyecta en la pantalla de la sala un tablero de CRM con todas las tarjetas apiladas en la primera columna y telarañas en las demás; Don Ramiro se atraganta con el café.
   - **Rubén:** "Jefe, este es nuestro CRM. Trescientos leads en «Nuevo»… desde marzo."
   - Sonido: tos, taza que se cae
2. Don Ramiro, con la camisa manchada de café, golpea la mesa; Rubén contesta sin inmutarse mientras Diego silba viendo al techo.
   - **Don Ramiro:** "¡¿Y cuánto estamos pagando por esto?!"
   - **Rubén:** "Lo de cada mes, jefe. Puntual."
   - Sonido: silbido de Diego

**Motor (narrador)**

- `photo` · Pagaste GoHighLevel, pero tus asesores viven en WhatsApp, no en el CRM. Por eso las tarjetas nunca se mueven.  
  Pantalla: Titular: UN CRM QUE [NADIE] LLENA. Foto de laptop con tablero vacío.
- `ui+crm` · Lead Master lee lo que pasa en los chats y en las llamadas de cada asesor y mueve el lead solo: contactado, cita, apartado.  
  Pantalla: Tarjeta de Diana Trejo pasa sola de «Nuevo» a «Cita agendada».
- `ui+note` · Las notas también se escriben solas con lo que se habló en la llamada. Tu asesor solo habla con clientes. Y tú abres el CRM y por fin dice la verdad.  
  Pantalla: Nota: «Busca 2 recámaras en la Del Valle, crédito aprobado, visita el sábado 11:00».

**Cierre:** Comenta CRM y te enseñamos el tuyo moviéndose solo.

## S49 · Aguacate Andrés y su «socio»

_circulos · P04 · Frutinovela · ~38 s · Comenta LEADS_

**Gancho en pantalla:** ¿TU ASESOR / TIENE [SOCIO]?

**Personas con IA**

1. Sala de juntas de frutas. Don Piña golpea la mesa; Aguacate Andrés esconde el celular detrás de la espalda y suda. Música de telenovela, zoom rápido.
   - **Don Piña:** "Aguacate, ¿por qué Diana Trejo dice que ya la atiende «tu socio»?"
   - **Aguacate Andrés:** "¿Socio? ¿Cuál socio? Yo no tengo socio."
   - Sonido: golpe en la mesa, violines
2. Limón abre la laptop despacio y la gira hacia Don Piña; Mango ahoga un grito, Fresa Valeria se tapa la boca. Trueno, triple zoom a Aguacate, que se empieza a poner café.
   - **Limón:** "Tengo el chat, Don Piña."
   - Sonido: trueno, golpe de piano

**Motor (narrador)**

- `chat` · Este es el chat que nunca ves, porque vive en el celular personal de tu asesor. Ahí se ofrecen otros proyectos, otras comisiones y otros socios.  
  Pantalla: Chat Andrés → Diana Trejo: «Mejor te atiendo por fuera con mi socio, te sale más barato la comisión».
- `stack` · Con Lead Master el WhatsApp de cada asesor está conectado, solo las conversaciones con leads. Y las llamadas salen del sistema y quedan grabadas.  
  Pantalla: Tarjetas: WhatsApp conectado (lo personal no) · Llamadas grabadas · Llamadas por fuera: 0.
- `ui+report` · Si un lead se queda sin seguimiento o pasa algo raro, te llega un aviso. Y si el asesor se va, el historial se queda contigo.  
  Pantalla: Aviso en WhatsApp: «Algo raro con Diana Trejo (Andrés M.)» · El historial se queda.

**Cierre:** Comenta LEADS antes de que tu Aguacate tenga socio.

## S50 · Llegó una demanda por un WhatsApp de Diego

_circulos · P07 · Junta · ~36 s · Comenta SISTEMA_

**Gancho en pantalla:** UN WHATSAPP, / UNA [DEMANDA]

**Personas con IA**

1. Rubén entra corriendo a la sala de juntas agitando un sobre; Don Ramiro escupe el café sobre la mesa.
   - **Rubén:** "¡Don Ramiro! ¡Llegó una demanda! ¡Por un WhatsApp de Diego!"
   - Sonido: puerta que se azota, escupitajo de café
2. Don Ramiro voltea despacio hacia Diego, que suda y sonríe nervioso; todos los demás se dan una palmada en la frente al mismo tiempo.
   - **Don Ramiro:** "Diego… ¿qué le escribiste a ese cliente?"
   - **Diego:** "Nada, jefe. Nomás que le garantizaba quince por ciento de plusvalía."
   - Sonido: cuatro palmadas al mismo tiempo

**Motor (narrador)**

- `case` · Cuando tu asesor promete algo por escrito desde el WhatsApp de la inmobiliaria, el cliente no demanda al asesor. Te demanda a ti.  
  Pantalla: Expediente: «Demanda por promesa de plusvalía garantizada» · Responsable: la inmobiliaria · sello.
- `photo` · Y casi siempre el dueño se entera cuando ya llegó la carta del abogado. Porque nadie lee los chats de los asesores hasta que hay un problema.  
  Pantalla: Titular: TE ENTERAS [TARDE]. Foto de escritorio de abogado.
- `mock` · Con Lead Master las conversaciones con leads viven en tu sistema: revisas qué se le prometió a cada cliente y te llega un aviso cuando algo raro pasa con un lead.  
  Pantalla: Conversación con la frase «te garantizo 15% de plusvalía» resaltada · aviso: «Algo raro con un lead de Diego H.».

**Cierre:** Comenta SISTEMA antes de que te llegue el sobre.

