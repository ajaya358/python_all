# HTTPS and Security Headers
# Security headers protect against common browser-based attacks

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# --- Security Headers Middleware ---
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"]    = "nosniff"
    response.headers["X-Frame-Options"]           = "DENY"
    response.headers["X-XSS-Protection"]          = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"]           = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"]   = "default-src 'self'"
    response.headers["Permissions-Policy"]        = "geolocation=(), microphone=()"
    return response

@app.get("/")
def root():
    return {"message": "Secure API"}

# --- What each header does ---
print("=== Security Headers Explained ===")
headers = {
    "X-Content-Type-Options: nosniff":          "Prevent MIME type sniffing",
    "X-Frame-Options: DENY":                    "Prevent clickjacking (no iframes)",
    "X-XSS-Protection: 1; mode=block":          "Enable browser XSS filter",
    "Strict-Transport-Security":                "Force HTTPS for 1 year",
    "Referrer-Policy":                          "Control referrer info sent",
    "Content-Security-Policy":                  "Control which resources can load",
    "Permissions-Policy":                       "Disable browser features (camera, mic)",
}
for h, desc in headers.items():
    print(f"  {h:45}: {desc}")

print("\n=== HTTPS Setup (Nginx + Let's Encrypt) ===")
print("""
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get free SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renew (add to crontab)
0 12 * * * certbot renew --quiet
""")

print("=== Environment Variables for Secrets ===")
print("""
# .env file (never commit to git!)
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/db
OPENAI_API_KEY=sk-...

# Load in Python
from dotenv import load_dotenv
import os
load_dotenv()
secret = os.getenv("SECRET_KEY")

# Add .env to .gitignore
echo ".env" >> .gitignore
""")

# Run: uvicorn https_headers:app --reload
