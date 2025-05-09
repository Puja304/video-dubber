import React from 'react';

export default function VideoPlayer({ videoSrc }) {

console.log("VideoPlayer rendered with videoSrc:", videoSrc);
  return (
    <div className="video-container" style={{ width: '60%', height: '55%', position: 'relative' }}>
      {videoSrc ? (
        <video
          controls
          style={{ 
            width: '100%',
            height: '100%',
            backgroundColor: '#000' ,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',

          }}
        >
          <source src={videoSrc} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      ) : (
        <div
          style={{
            width: '100%',
            height: '100%',
            backgroundColor: '#e0e0e0',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            color: '#9333EA',
            fontFamily: 'Poppins, sans-serif',
            borderRadius: '8px',
          }}
        >
          Upload a video to preview
        </div>
      )}
    </div>
  );
}
