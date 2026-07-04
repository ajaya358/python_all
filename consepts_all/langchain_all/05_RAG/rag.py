# RAG - Retrieval Augmented Generation
# Give LLM access to YOUR documents so it answers from your data
# pip install langchain langchain-openai chromadb sentence-transformers

print("=== What is RAG? ===")
print("  Problem: LLM doesn't know your company docs, private data, recent events")
print("  Solution: Store your docs in vector DB → retrieve relevant chunks → send to LLM\n")

print("=== RAG Pipeline Steps ===")
steps = [
    "1. LOAD      → Load documents (PDF, CSV, web, DB)",
    "2. SPLIT     → Split into small chunks (500-1000 chars)",
    "3. EMBED     → Convert chunks to vectors (numbers)",
    "4. STORE     → Save vectors in vector DB (ChromaDB, FAISS, Pinecone)",
    "5. RETRIEVE  → User asks question → find similar chunks",
    "6. GENERATE  → Send question + chunks to LLM → get answer",
]
for step in steps:
    print(f"  {step}")

# --- Manual RAG simulation (no API key needed) ---
print("\n=== Manual RAG Simulation ===")
import math

# Step 1: Documents
documents = [
    {"id": 1, "text": "Python is a high-level programming language used for AI and web development."},
    {"id": 2, "text": "FastAPI is a modern Python web framework for building REST APIs quickly."},
    {"id": 3, "text": "Machine learning is teaching computers to learn patterns from data."},
    {"id": 4, "text": "Docker is a tool to package applications into containers for easy deployment."},
    {"id": 5, "text": "Redis is an in-memory database used for caching and session management."},
]

# Step 2: Simple keyword-based retrieval (real RAG uses embeddings)
def retrieve(query: str, docs: list, top_k: int = 2):
    query_words = set(query.lower().split())
    scored = []
    for doc in docs:
        doc_words = set(doc["text"].lower().split())
        score = len(query_words & doc_words)
        scored.append((score, doc))
    scored.sort(reverse=True)
    return [doc for _, doc in scored[:top_k]]

# Step 3: Generate answer using retrieved context
def rag_answer(query: str):
    relevant_docs = retrieve(query, documents)
    context = "\n".join([d["text"] for d in relevant_docs])
    print(f"  Query: {query}")
    print(f"  Retrieved context:\n    {context}")
    print(f"  (LLM would now answer using this context)\n")

rag_answer("What is Python used for?")
rag_answer("How does Docker work?")

print("=== Real LangChain RAG Code ===")
rag_code = """
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load and split
loader = PyPDFLoader("document.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embed and store
vectorstore = Chroma.from_documents(chunks, OpenAIEmbeddings())

# RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)
answer = qa_chain.invoke("What is the main topic of this document?")
print(answer)
"""
print(rag_code)
