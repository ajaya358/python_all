# LangChain - Framework for building LLM-powered applications
# pip install langchain langchain-openai langchain-community

print("=== What is LangChain? ===")
concepts = {
    "LangChain":      "Framework to build apps using LLMs (GPT, Claude, Gemini)",
    "Chain":          "Sequence of steps: prompt → LLM → output → next step",
    "Prompt Template":"Reusable prompt with variables: 'Translate {text} to {language}'",
    "LLM":            "The AI model (OpenAI, Anthropic, HuggingFace, Ollama)",
    "Memory":         "Stores conversation history so LLM remembers context",
    "Agent":          "LLM that decides which tool to use to answer a question",
    "Tool":           "Function the agent can call (search, calculator, DB query)",
    "RAG":            "Retrieval Augmented Generation — give LLM your own documents",
    "Vector Store":   "Database that stores embeddings for semantic search",
    "Document Loader":"Load data from PDF, CSV, web, DB into LangChain",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== LangChain Components ===")
components = [
    "Models      → LLMs and Chat Models (OpenAI, Ollama, HuggingFace)",
    "Prompts     → PromptTemplate, ChatPromptTemplate, FewShotPrompt",
    "Chains      → LLMChain, SequentialChain, ConversationChain",
    "Memory      → ConversationBufferMemory, ConversationSummaryMemory",
    "Agents      → ReAct, OpenAI Functions, Tool Calling agents",
    "Tools       → Search, Calculator, Python REPL, custom tools",
    "Retrievers  → Vector store retriever for RAG",
    "Loaders     → PDF, CSV, Web, YouTube, Notion loaders",
    "Splitters   → Split large docs into chunks for embedding",
]
for c in components:
    print(f"  {c}")

print("\n=== Install ===")
print("  pip install langchain langchain-openai langchain-community chromadb")
print("  Set: OPENAI_API_KEY=your-key  (or use Ollama for free local LLM)")
print("  Ollama: https://ollama.ai  →  ollama pull llama3")
