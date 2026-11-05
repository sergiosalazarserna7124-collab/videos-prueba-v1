import React from 'react';
import {Composition} from 'remotion';
import {Reel, ReelProps} from './Reel';

const empty: ReelProps = {id: 'empty', totalFrames: 60, scenes: [], words: []};

export const Root: React.FC = () => (
  <Composition
    id="Reel"
    component={Reel as any}
    width={1080}
    height={1920}
    fps={30}
    durationInFrames={60}
    defaultProps={empty as any}
    calculateMetadata={({props}) => ({durationInFrames: Math.max(30, (props as any).totalFrames ?? 60)})}
  />
);
