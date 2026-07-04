# LangChain Prompts - PromptTemplate and ChatPromptTemplate
# pip install langchain langchain-openai
# Set env: OPENAI_API_KEY=your-key  OR use Ollama (free)

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts import FewShotPromptTemplate

# --- 1. Basic PromptTemplate ---
print("=== PromptTemplate ===")
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms for a beginner."
)
prompt = template.format(topic="machine learning")
print(prompt)

# --- 2. Multiple variables ---
print("\n=== Multi-variable Template ===")
translate_template = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following text to {language}:\n\n{text}"
)
prompt2 = translate_template.format(text="Hello, how are you?", language="Tamil")
print(prompt2)

# --- 3. ChatPromptTemplate (for chat models) ---
print("\n=== ChatPromptTemplate ===")
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {role}. Answer in {language}."),
    ("human", "{question}"),
])
messages = chat_template.format_messages(
    role="Python tutor",
    language="simple English",
    question="What is a decorator?"
)
for msg in messages:
    print(f"  {msg.type}: {msg.content}")

# --- 4. Few-shot prompt ---
print("\n=== Few-Shot Prompt ===")
examples = [
    {"input": "happy",   "output": "sad"},
    {"input": "tall",    "output": "short"},
    {"input": "fast",    "output": "slow"},
]
example_template = PromptTemplate(
    input_variables=["input", "output"],
    template="Word: {input} → Antonym: {output}"
)
few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    suffix="Word: {input} → Antonym:",
    input_variables=["input"]
)
print(few_shot.format(input="hot"))

# --- With real LLM (uncomment when you have API key or Ollama) ---
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-3.5-turbo")
# chain = template | llm
# response = chain.invoke({"topic": "neural networks"})
# print(response.content)
