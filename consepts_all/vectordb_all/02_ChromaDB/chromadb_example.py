# ChromaDB - Local vector database, easiest to start with
# pip install chromadb sentence-transformers

print("=== ChromaDB Setup ===")
print("""
import chromadb
from chromadb.utils import embedding_functions

# --- In-memory (for testing) ---
client = chromadb.Client()

# --- Persistent (saves to disk) ---
# client = chromadb.PersistentClient(path="./chroma_db")

# Use sentence-transformers for free embeddings (no API key)
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create collection
collection = client.create_collection(
    name="my_docs",
    embedding_function=embedding_fn
)

# --- Add documents ---
collection.add(
    documents=[
        "Python is a high-level programming language used for AI and web.",
        "FastAPI is a modern Python framework for building REST APIs.",
        "Machine learning teaches computers to learn from data.",
        "Docker packages apps into containers for easy deployment.",
        "Redis is an in-memory database used for caching.",
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
    metadatas=[
        {"source": "python_docs", "topic": "python"},
        {"source": "fastapi_docs", "topic": "web"},
        {"source": "ml_docs", "topic": "ml"},
        {"source": "docker_docs", "topic": "devops"},
        {"source": "redis_docs", "topic": "database"},
    ]
)

# --- Query (semantic search) ---
results = collection.query(
    query_texts=["best language for artificial intelligence"],
    n_results=2
)
print("Query: best language for artificial intelligence")
print("Results:", results["documents"])
print("Metadata:", results["metadatas"])

# --- Get by ID ---
doc = collection.get(ids=["doc1"])
print("Get doc1:", doc["documents"])

# --- Update ---
collection.update(ids=["doc1"], documents=["Python updated description"])

# --- Delete ---
collection.delete(ids=["doc5"])

# --- Count ---
print("Total docs:", collection.count())
""")

print("=== Key Points ===")
points = [
    "ChromaDB auto-embeds text — no manual embedding needed",
    "Persistent client saves data between runs",
    "Metadata helps filter results (by topic, date, source)",
    "n_results controls how many similar docs to return",
    "Free embeddings with sentence-transformers (no API key)",
]
for p in points:
    print(f"  - {p}")
