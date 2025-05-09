import React, { useState } from 'react';
import Header from './Header';
import LangSelection from './LangSelection';
import UpDown from './UpDown';
import VideoPlayer from './VideoPlayer';

export default function MainPage() {
  const [dubTo, setDubTo] = useState('English');
  const [videoSrc, setVideoSrc] = useState(null);
  const [dubbedSrc, setDubbedSrc] = useState(null);

  const languagesSupported = [
    { label: 'English', code: 'en' },
    { label: 'French', code: 'fr' },
    { label: 'Portugese', code: 'pr' }
  ];

  const handleLanguageSelection = (lang) => {
    setDubTo(lang);
  };

let currentBlobUrl = null;

const handleUpload = async (file) => {
    let BASE_URL = "https://dubify-jflc.onrender.com";
    const formData = new FormData();
    formData.append("video", file);
    formData.append("language", dubTo);

    try {
        const res = await fetch("https://dubify-jflc.onrender.com/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        console.log(" Backend responded with:", data);

        // fetch the processed video as blob
        const videoResponse = await fetch(`https://dubify-jflc.onrender.com/videos/${data.processed_filename}`);
        const videoBlob = await videoResponse.blob();

        // revoke previous blob url if it exists
        if (currentBlobUrl) {
            URL.revokeObjectURL(currentBlobUrl);
        }
        // create and set new blob URL
        const blobUrl = URL.createObjectURL(videoBlob);
        currentBlobUrl = blobUrl; // store it for next time
        setDubbedSrc(blobUrl);
    } catch (err) {
        console.error("Upload failed:", err);
    }
};

  const handleDownload = () => {
    if (!dubbedSrc) return;
    if (navigator.userAgent.includes("Safari") && !navigator.userAgent.includes("Chrome")) {
        window.open(dubbedSrc, '_blank');
    } else {
        const a = document.createElement('a');
        a.href = dubbedSrc;
        a.download = 'dubbed_video.mp4';
        a.target = '_self';
        a.rel = 'noopener noreferrer';
        a.click();
    }
};

  return (
    <div className="main-page">
      <Header />
      <LangSelection
        languages={languagesSupported}
        selectedLanguage={dubTo}
        onSelectLanguage={handleLanguageSelection}
      />
      <UpDown isUp={true} onClick={handleUpload} />
      <VideoPlayer videoSrc={dubbedSrc} />
      <UpDown isUp={false} onClick={handleDownload} />
    </div>
  );
}
