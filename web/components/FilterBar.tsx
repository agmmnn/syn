import React from "react";
import { CATEGORIES } from "../lib/datamuse";

interface FilterBarProps {
  active: string;
  onChange: (category: string) => void;
  visibleCategories: string[];
}

export function FilterBar({
  active,
  onChange,
  visibleCategories,
}: FilterBarProps) {
  const allCategories = ["All", ...Object.keys(CATEGORIES)];

  return (
    <div className="filter-bar">
      {allCategories.map((cat) => {
        const isAll = cat === "All";
        const hasResults = isAll || visibleCategories.includes(cat);

        if (!isAll && !hasResults) return null;

        return (
          <button
            key={cat}
            className={`filter-pill ${active === cat ? "active" : ""}`}
            onClick={() => onChange(cat)}
          >
            {cat}
          </button>
        );
      })}
    </div>
  );
}
