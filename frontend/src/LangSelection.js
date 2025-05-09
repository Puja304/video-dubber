import React from "react";

export default function LangSelection({ languages, selectedLanguage, onSelectLanguage }) {
  return (
    <div className="lang-selection">
      <h4>Dub to:</h4>
      <div className="lang-list">
      {languages.map((lang) => (
        <button
            key={lang}
            className="lang-button"
            style={{
            backgroundColor: lang.label === selectedLanguage ? '#FACC15' : '#9333EA',
            color: lang.code === selectedLanguage ? 'black' : 'white'
            }}
            onClick={() => onSelectLanguage(lang.label)}
        >
            {lang.label}
        </button>
        ))}

      </div>
    </div>
  );
}
