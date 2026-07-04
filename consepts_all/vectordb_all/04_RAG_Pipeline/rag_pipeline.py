# Full RAG Pipeline - Load → Embed → Store → Retrieve → Generate
# pip install langchain langchain-openai chromadb sentence-transformers

print("=== Complete RAG Pipeline ===")
print("""
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# ── Step 1: Load documents ──────────────────────────────────────
loader = TextLoader("my_document.txt")          # or PyPDFLoader("file.pdf")
documents = loader.load()

# ── Step 2: Split into chunks ───────────────────────────────────
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # max chars per chunk
    chunk_overlap=50,     # overlap to preserve context
)
chunks = splitter.split_documents(documents)
print(f"Total chunks: {len(chunks)}")

# ── Step 3: Embed and store in ChromaDB ────────────────────────
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# ── Step 4: Create retriever ────────────────────────────────────
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}   # return top 3 chunks
)

# ── Step 5: Custom prompt for RAG ──────────────────────────────
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=\\"\\"\\"
    Use the following context to answer the question.
    If you don't know the answer, say 'I don't know'.

    Context: {context}

    Question: {question}

    Answer:
    \\"\\"\\"
)

# ── Step 6: RAG chain ───────────────────────────────────────────
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)

# ── Step 7: Ask questions ───────────────────────────────────────
result = qa_chain.invoke({"query": "What is the main topic?"})
print("Answer:", result["result"])
print("Sources:", [doc.metadata for doc in result["source_documents"]])
""")

print("=== RAG Tips ===")
tips = [
    "chunk_size=500 is good for most docs, increase for code",
    "chunk_overlap=50 prevents losing context at chunk boundaries",
    "k=3 retrieves 3 chunks — more chunks = more context but more tokens",
    "Use temperature=0 for factual RAG answers",
    "Add metadata (filename, page) to track sources",
    "Use SentenceTransformer embeddings (free) or OpenAI embeddings (paid)",
]
for t in tips:
    print(f"  - {t}")
