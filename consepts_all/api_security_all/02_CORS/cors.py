# CORS - Cross-Origin Resource Sharing
# Controls which domains can call your API
# pip install fastapi uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- CORS Setup ---
# Development: allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # allow all (dev only)
    allow_credentials=True,
    allow_methods=["*"],           # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],           # Authorization, Content-Type, etc.
)

# --- Production: restrict to specific origins ---
# allowed_origins = [
#     "https://myapp.com",
#     "https://www.myapp.com",
#     "http://localhost:3000",     # React dev server
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=allowed_origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Authorization", "Content-Type"],
# )

@app.get("/")
def root():
    return {"message": "CORS configured"}

# --- What CORS does ---
print("=== What is CORS? ===")
print("  Browser blocks requests from different origins by default")
print("  Example: React app on localhost:3000 calling API on localhost:8000")
print("  CORS headers tell browser: 'this origin is allowed'\n")

print("=== CORS Headers ===")
headers = {
    "Access-Control-Allow-Origin":      "Which origins can access",
    "Access-Control-Allow-Methods":     "Which HTTP methods allowed",
    "Access-Control-Allow-Headers":     "Which request headers allowed",
    "Access-Control-Allow-Credentials": "Allow cookies/auth headers",
    "Access-Control-Max-Age":           "How long to cache preflight",
}
for h, desc in headers.items():
    print(f"  {h:40}: {desc}")

# Run: uvicorn cors:app --reload
