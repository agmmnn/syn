import React from "react";
import type { CategoryResult } from "../lib/datamuse";
import { CATEGORY_COLORS } from "../lib/datamuse";

interface ResultsProps {
  results: CategoryResult[];
  onWordClick: (word: string) => void;
  onWordCopy: (word: string) => void;
}

export function Results({ results, onWordClick, onWordCopy }: ResultsProps) {
  if (results.length === 0) {
    return (
      <div className="no-results">
        <p className="no-results-text">no words found — try another search</p>
      </div>
    );
  }

  return (
    <div className="results">
      {results.map((group, index) => (
        <div
          key={group.category}
          className="category-section"
          style={{ animationDelay: `${index * 0.06}s` }}
        >
          <div className="category-header">
            <span
              className="category-dot"
              style={{ background: CATEGORY_COLORS[group.category] }}
            />
            <h2 className="category-name">{group.category}</h2>
            <span className="category-count">{group.items.length}</span>
          </div>
          <div className="category-words">
            {group.items.map((word) => (
              <button
                key={word}
                className="word-chip"
                onClick={() => onWordClick(word)}
                onContextMenu={(e) => {
                  e.preventDefault();
                  onWordCopy(word);
                }}
                title={`Click to explore · Right-click to copy`}
              >
                {word}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
