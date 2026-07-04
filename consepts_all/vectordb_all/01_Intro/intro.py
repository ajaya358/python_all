# Vector Databases - Store and search embeddings
# Used in RAG, semantic search, recommendation systems

print("=== What is a Vector Database? ===")
concepts = {
    "Vector":        "List of numbers representing meaning of text/image",
    "Embedding":     "Converting text → vector using an AI model",
    "Vector DB":     "Database optimized to store and search vectors",
    "Similarity":    "Find vectors closest to query vector (semantic search)",
    "Index":         "Data structure for fast vector search (HNSW, IVF)",
    "Collection":    "Group of vectors (like a table in SQL)",
    "Metadata":      "Extra info stored with each vector (source, date, etc.)",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== Popular Vector Databases ===")
dbs = {
    "ChromaDB":  "Open source, runs locally, easy to use — best for learning",
    "FAISS":     "Facebook AI, fast, runs in memory — best for small datasets",
    "Pinecone":  "Managed cloud service, scalable — best for production",
    "Weaviate":  "Open source, GraphQL API, hybrid search",
    "Qdrant":    "Open source, Rust-based, very fast",
    "pgvector":  "PostgreSQL extension — add vector search to existing DB",
}
for db, desc in dbs.items():
    print(f"  {db:12}: {desc}")

print("\n=== How Vector Search Works ===")
steps = [
    "1. Text: 'Python is great for AI'",
    "2. Embed: model.encode(text) → [0.23, -0.45, 0.87, ...]",
    "3. Store: vectordb.add(vector, metadata={'source': 'doc1'})",
    "4. Query: user asks 'best language for machine learning'",
    "5. Embed query → search DB for nearest vectors",
    "6. Return top-k most similar documents",
]
for s in steps:
    print(f"  {s}")

print("\n=== Install ===")
print("  pip install chromadb sentence-transformers faiss-cpu")
