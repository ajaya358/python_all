# FAISS - Facebook AI Similarity Search
# Fast in-memory vector search, great for large datasets
# pip install faiss-cpu sentence-transformers numpy

print("=== What is FAISS? ===")
print("  FAISS = Facebook AI Similarity Search")
print("  Stores vectors in memory, extremely fast search")
print("  Best for: millions of vectors, local use, no server needed\n")

print("=== FAISS with Sentence Transformers ===")
print("""
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# --- Documents ---
documents = [
    "Python is a programming language for AI and web development.",
    "FastAPI is a fast Python web framework.",
    "Machine learning teaches computers to learn from data.",
    "Docker packages apps into containers.",
    "Redis is used for caching and sessions.",
]

# --- Create embeddings ---
embeddings = model.encode(documents)
embeddings = np.array(embeddings).astype("float32")
print("Embedding shape:", embeddings.shape)  # (5, 384)

# --- Build FAISS index ---
dimension = embeddings.shape[1]  # 384
index = faiss.IndexFlatL2(dimension)  # L2 = Euclidean distance
index.add(embeddings)
print("Total vectors in index:", index.ntotal)

# --- Search ---
query = "best language for machine learning"
query_vector = model.encode([query]).astype("float32")

k = 2  # return top 2 results
distances, indices = index.search(query_vector, k)

print(f"\\nQuery: {query}")
for i, idx in enumerate(indices[0]):
    print(f"  Result {i+1}: {documents[idx]} (distance: {distances[0][i]:.4f})")

# --- Save and load index ---
faiss.write_index(index, "my_index.faiss")
loaded_index = faiss.read_index("my_index.faiss")
""")

print("=== FAISS Index Types ===")
index_types = {
    "IndexFlatL2":    "Exact search, L2 distance — accurate but slow for large data",
    "IndexFlatIP":    "Exact search, inner product (cosine similarity)",
    "IndexIVFFlat":   "Approximate search — faster, slight accuracy loss",
    "IndexHNSWFlat":  "Graph-based, very fast approximate search",
}
for k, v in index_types.items():
    print(f"  {k:18}: {v}")
