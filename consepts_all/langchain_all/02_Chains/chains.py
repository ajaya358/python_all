# LangChain Chains - Connect prompt → LLM → output → next step
# pip install langchain langchain-openai

print("=== What is a Chain? ===")
print("  Chain = Prompt Template | LLM | Output Parser")
print("  LCEL (LangChain Expression Language): use | to connect components\n")

# --- Concept: Manual chain simulation (no API key needed) ---
class FakeLLM:
    """Simulates LLM response for learning"""
    def invoke(self, prompt):
        if "explain" in prompt.lower():
            return type("R", (), {"content": f"Here is a simple explanation of the topic in your prompt."})()
        if "translate" in prompt.lower():
            return type("R", (), {"content": "Translated text here."})()
        return type("R", (), {"content": f"Response to: {prompt[:50]}..."})()

class SimpleChain:
    def __init__(self, template, llm):
        self.template = template
        self.llm = llm

    def invoke(self, inputs: dict):
        prompt = self.template
        for k, v in inputs.items():
            prompt = prompt.replace("{" + k + "}", v)
        return self.llm.invoke(prompt)

llm = FakeLLM()

print("=== Simple Chain ===")
chain1 = SimpleChain("Explain {topic} in simple terms.", llm)
result = chain1.invoke({"topic": "Python decorators"})
print(f"  Result: {result.content}")

print("\n=== Sequential Chain (output of one → input of next) ===")
# Step 1: Generate outline
# Step 2: Write content from outline
# Step 3: Summarize content
steps = [
    "Step 1: Generate outline for topic",
    "Step 2: Write full content from outline",
    "Step 3: Summarize content to 3 lines",
]
for step in steps:
    print(f"  {step}")

print("\n=== Real LangChain LCEL Syntax ===")
lcel_code = """
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Simple chain
prompt = ChatPromptTemplate.from_template("Explain {topic} simply.")
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"topic": "machine learning"})
print(result)

# Sequential chain
summarize_prompt = ChatPromptTemplate.from_template("Summarize: {text}")
full_chain = (
    prompt
    | llm
    | StrOutputParser()
    | (lambda text: {"text": text})
    | summarize_prompt
    | llm
    | StrOutputParser()
)
result = full_chain.invoke({"topic": "neural networks"})
print(result)
"""
print(lcel_code)
