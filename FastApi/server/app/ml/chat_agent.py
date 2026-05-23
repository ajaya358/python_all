"""A simple chat-like agent that learns from text and answers by retrieval."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class ChatAgent:
    memory: List[str] = field(default_factory=list)
    vectorizer: Optional[TfidfVectorizer] = None
    embeddings: Optional[np.ndarray] = None

    def learn_text(self, text: str) -> None:
        """Add text to memory and update embeddings."""
        if not text:
            return
        self.memory.append(text)
        self._update_embeddings()

    def _update_embeddings(self) -> None:
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.embeddings = self.vectorizer.fit_transform(self.memory).toarray()

    def ask(self, question: str, top_k: int = 1) -> str:
        """Answer by retrieving the most similar learned text."""
        if not self.memory or not question:
            return "I have not learned anything yet or your question is empty."

        if self.vectorizer is None or self.embeddings is None:
            self._update_embeddings()

        query_vec = self.vectorizer.transform([question]).toarray()
        scores = cosine_similarity(query_vec, self.embeddings)[0]
        top_indices = np.argsort(scores)[::-1][:top_k]
        answers = [self.memory[idx] for idx in top_indices if scores[idx] > 0]

        if not answers:
            return "I could not find an answer. Please teach me more."

        return "\n---\n".join(answers)

    def clear_memory(self) -> None:
        """Remove all learned text."""
        self.memory.clear()
        self.vectorizer = None
        self.embeddings = None
