# API Security - Protect your API from attacks
# Every production API must implement these

print("=== Common API Security Threats ===")
threats = {
    "SQL Injection":        "Attacker sends SQL in input to manipulate DB",
    "XSS":                  "Cross-Site Scripting — inject malicious JS",
    "CSRF":                 "Cross-Site Request Forgery — trick user to make requests",
    "Broken Auth":          "Weak tokens, no expiry, exposed credentials",
    "Rate Limiting bypass": "Flood API with requests (DDoS)",
    "Sensitive Data Leak":  "Passwords/keys in logs, responses, or URLs",
    "IDOR":                 "Access other users' data by changing ID in URL",
    "Injection":            "Command injection, LDAP injection, etc.",
}
for k, v in threats.items():
    print(f"  {k:25}: {v}")

print("\n=== Security Checklist ===")
checklist = [
    "✅ Use HTTPS (never HTTP in production)",
    "✅ Hash passwords with bcrypt (never store plain text)",
    "✅ Use JWT with short expiry (15-30 min)",
    "✅ Validate all input with Pydantic",
    "✅ Add rate limiting to all endpoints",
    "✅ Set CORS to allow only trusted origins",
    "✅ Add security headers (X-Frame-Options, CSP, etc.)",
    "✅ Never expose stack traces in error responses",
    "✅ Use parameterized queries (SQLAlchemy handles this)",
    "✅ Store secrets in environment variables, not in code",
    "✅ Log security events (failed logins, suspicious activity)",
    "✅ Use RBAC — users only access their own data",
]
for item in checklist:
    print(f"  {item}")

print("\n=== OWASP Top 10 API Risks ===")
owasp = [
    "1. Broken Object Level Authorization (BOLA/IDOR)",
    "2. Broken Authentication",
    "3. Broken Object Property Level Authorization",
    "4. Unrestricted Resource Consumption (no rate limiting)",
    "5. Broken Function Level Authorization",
    "6. Unrestricted Access to Sensitive Business Flows",
    "7. Server Side Request Forgery (SSRF)",
    "8. Security Misconfiguration",
    "9. Improper Inventory Management",
    "10. Unsafe Consumption of APIs",
]
for item in owasp:
    print(f"  {item}")
