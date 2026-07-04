# Azure AI Services - OpenAI, Speech, Vision, Language
# pip install openai azure-cognitiveservices-speech

print("=== Azure AI Services ===")
services = {
    "Azure OpenAI":         "GPT-4, GPT-3.5, DALL-E, Whisper via Azure (enterprise grade)",
    "Azure AI Search":      "Cognitive search with vector search + RAG support",
    "Azure AI Vision":      "Image analysis, OCR, face detection",
    "Azure AI Speech":      "Speech-to-text, text-to-speech",
    "Azure AI Language":    "Sentiment analysis, NER, translation",
    "Azure AI Document":    "Extract data from PDFs, forms, invoices",
    "Azure ML":             "Train, deploy, manage ML models",
    "Azure AI Studio":      "Build and deploy AI apps (like AWS Bedrock)",
}
for k, v in services.items():
    print(f"  {k:24}: {v}")

print("\n=== Azure OpenAI (GPT-4) ===")
print("""
# pip install openai
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://myresource.openai.azure.com/",
    api_key="your-azure-openai-key",
    api_version="2024-02-01"
)

# Chat completion
response = client.chat.completions.create(
    model="gpt-4",           # your deployment name
    messages=[
        {"role": "system", "content": "You are a helpful Python tutor."},
        {"role": "user",   "content": "Explain decorators in Python."}
    ],
    temperature=0.7,
    max_tokens=500
)
print(response.choices[0].message.content)

# Embeddings
embedding = client.embeddings.create(
    model="text-embedding-ada-002",
    input="Python is a great programming language"
)
vector = embedding.data[0].embedding
print(f"Vector dimensions: {len(vector)}")  # 1536
""")

print("=== Azure AI Search (RAG) ===")
print("""
# pip install azure-search-documents
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential

search_client = SearchClient(
    endpoint="https://mysearch.search.windows.net",
    index_name="my-index",
    credential=AzureKeyCredential("your-search-key")
)

# Keyword search
results = search_client.search(search_text="Python FastAPI")
for r in results:
    print(r["title"], r["@search.score"])

# Vector search (semantic)
query_vector = get_embedding("Python web framework")  # your embedding function
vector_query = VectorizedQuery(vector=query_vector, k_nearest_neighbors=3, fields="content_vector")
results = search_client.search(search_text=None, vector_queries=[vector_query])
""")

print("=== Azure AI Vision ===")
print("""
# pip install azure-ai-vision-imageanalysis
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

client = ImageAnalysisClient(
    endpoint="https://myresource.cognitiveservices.azure.com/",
    credential=AzureKeyCredential("your-key")
)

result = client.analyze_from_url(
    image_url="https://example.com/image.jpg",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS, VisualFeatures.TEXT]
)
print("Caption:", result.caption.text)
print("Tags:", [t.name for t in result.tags.list])
""")
