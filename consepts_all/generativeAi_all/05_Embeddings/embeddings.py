# Embeddings - Converting text to numbers (vectors)
# Embeddings let AI understand meaning and similarity between words/sentences

import math

# --- Concept: What is an embedding? ---
print("=== What are Embeddings? ===")
print("Text → [0.23, -0.45, 0.87, ...]  (a list of numbers = vector)")
print("Similar words have similar vectors\n")

# --- Manual simple word vectors (for learning) ---
word_vectors = {
    "king":   [1.0, 0.9, 0.1],
    "queen":  [0.9, 1.0, 0.1],
    "man":    [0.8, 0.2, 0.1],
    "woman":  [0.7, 0.3, 0.1],
    "python": [0.1, 0.1, 1.0],
    "java":   [0.1, 0.2, 0.9],
}

# Cosine similarity: measures how similar two vectors are (1 = same, 0 = different)
def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x**2 for x in a))
    mag_b = math.sqrt(sum(x**2 for x in b))
    return round(dot / (mag_a * mag_b), 3)

print("=== Similarity Scores ===")
pairs = [("king", "queen"), ("king", "python"), ("python", "java"), ("man", "woman")]
for w1, w2 in pairs:
    score = cosine_similarity(word_vectors[w1], word_vectors[w2])
    print(f"  {w1} vs {w2}: {score}")

# --- Use case of embeddings ---
print("\n=== Use Cases ===")
uses = [
    "Semantic search (find similar documents)",
    "Recommendation systems",
    "Clustering similar texts",
    "Question answering (RAG)",
]
for u in uses:
    print(f"  - {u}")

# Real embeddings: pip install sentence-transformers
# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer('all-MiniLM-L6-v2')
# vector = model.encode("Hello world")
