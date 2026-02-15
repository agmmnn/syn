import React, { useState, useEffect, useCallback } from "react";
import { createRoot } from "react-dom/client";
import { SearchBar } from "./components/SearchBar";
import { FilterBar } from "./components/FilterBar";
import { Results } from "./components/Results";
import { Toast, useToast } from "./components/Toast";
import { fetchAll, CategoryResult } from "./lib/datamuse";
import "./styles/app.css";

function getQueryParam(): string {
  const params = new URLSearchParams(window.location.search);
  return params.get("q") ?? "";
}

function setQueryParam(word: string) {
  const url = new URL(window.location.href);
  if (word) {
    url.searchParams.set("q", word);
  } else {
    url.searchParams.delete("q");
  }
  window.history.pushState({}, "", url.toString());
}

function App() {
  const [input, setInput] = useState(getQueryParam);
  const [query, setQuery] = useState(getQueryParam);
  const [results, setResults] = useState<CategoryResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [filter, setFilter] = useState("All");
  const { toast, show: showToast } = useToast();

  const search = useCallback(
    async (word: string) => {
      const trimmed = word.trim();
      if (!trimmed) return;

      setQuery(trimmed);
      setInput(trimmed);
      setQueryParam(trimmed);
      setLoading(true);
      setHasSearched(true);
      setFilter("All");

      const data = await fetchAll(trimmed);
      setResults(data);
      setLoading(false);
    },
    [],
  );

  // Initial load from URL
  useEffect(() => {
    const q = getQueryParam();
    if (q) search(q);
  }, []);

  // Handle browser back/forward
  useEffect(() => {
    const handlePop = () => {
      const q = getQueryParam();
      if (q) search(q);
      else {
        setInput("");
        setQuery("");
        setResults([]);
        setHasSearched(false);
      }
    };
    window.addEventListener("popstate", handlePop);
    return () => window.removeEventListener("popstate", handlePop);
  }, [search]);

  const handleReset = (e: React.MouseEvent) => {
    e.preventDefault();
    setInput("");
    setQuery("");
    setResults([]);
    setHasSearched(false);
    setFilter("All");
    setQueryParam("");
  };

  const handleSubmit = () => search(input);

  const handleWordClick = (word: string) => search(word);

  const handleWordCopy = async (word: string) => {
    await navigator.clipboard.writeText(word);
    showToast(`copied "${word}"`);
  };

  const filteredResults =
    filter === "All"
      ? results
      : results.filter((r) => r.category === filter);

  const visibleCategories = results.map((r) => r.category);

  return (
    <div className={`app ${hasSearched ? "app--compact" : ""}`}>
      <header className="header">
        <a href="/" className="header-link" onClick={handleReset}>
          <h1 className="header-title">
            syn<span>🌾</span>
          </h1>
          <p className="header-subtitle">word explorer</p>
        </a>
      </header>

      <SearchBar value={input} onChange={setInput} onSubmit={handleSubmit} />

      {hasSearched && !loading && results.length > 0 && (
        <FilterBar
          active={filter}
          onChange={setFilter}
          visibleCategories={visibleCategories}
        />
      )}

      {loading ? (
        <div className="loading">
          <div className="loading-dots">
            <div className="loading-dot" />
            <div className="loading-dot" />
            <div className="loading-dot" />
          </div>
        </div>
      ) : hasSearched ? (
        <Results
          results={filteredResults}
          onWordClick={handleWordClick}
          onWordCopy={handleWordCopy}
        />
      ) : (
        <div className="empty-state">
          <div className="empty-state-icon">🌾</div>
          <p className="empty-state-text">
            type a word to explore its connections
          </p>
        </div>
      )}

      <footer className="footer">
        <p>
          powered by{" "}
          <a href="https://www.datamuse.com/api/" target="_blank" rel="noopener">
            Datamuse API
          </a>{" "}
          ·{" "}
          <a href="https://github.com/agmmnn/syn" target="_blank" rel="noopener">
            GitHub
          </a>
        </p>
      </footer>

      <Toast message={toast.message} visible={toast.visible} />
    </div>
  );
}

const root = createRoot(document.getElementById("root")!);
root.render(<App />);
