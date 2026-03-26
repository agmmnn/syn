import React, { useRef, useEffect } from "react";

interface SearchBarProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
}

export function SearchBar({ value, onChange, onSubmit }: SearchBarProps) {
  const inputRef = useRef<HTMLInputElement>(null);
  const inputId = "word-search";

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      e.preventDefault();
      onSubmit();
    }
  };

  return (
    <div className="search-container">
      <label className="search-label" htmlFor={inputId}>
        Search for a word
      </label>
      <div className="search-field">
        <input
          id={inputId}
          ref={inputRef}
          type="search"
          className="search-input"
          placeholder="explore a word…"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={handleKeyDown}
          spellCheck={false}
          autoComplete="off"
        />
        <button
          className="search-submit"
          onClick={onSubmit}
          aria-label="Search"
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <line x1="5" y1="12" x2="19" y2="12" />
            <polyline points="12 5 19 12 12 19" />
          </svg>
        </button>
      </div>
      <div className="search-meta">
        <p className="search-hint">
          try <em>word:topic</em> for guided results, like{" "}
          <em>medium:size</em> or <em>medium:media</em>
        </p>
        <span className="search-shortcut">Press Enter</span>
      </div>
    </div>
  );
}
