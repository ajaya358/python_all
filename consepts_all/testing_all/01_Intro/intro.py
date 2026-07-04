# Testing - Verify your code works correctly
# pip install pytest

print("=== Why Testing? ===")
print("  - Catch bugs before they reach production")
print("  - Refactor code confidently")
print("  - Document how code should behave")
print("  - Required in every professional project\n")

print("=== Types of Tests ===")
test_types = {
    "Unit Test":        "Test one function in isolation — fast, no DB/network",
    "Integration Test": "Test multiple components together — DB, API, services",
    "End-to-End Test":  "Test full user flow — browser to DB and back",
    "Regression Test":  "Ensure old features still work after new changes",
    "Load Test":        "Test performance under high traffic (locust, k6)",
}
for k, v in test_types.items():
    print(f"  {k:20}: {v}")

print("\n=== Testing Tools in Python ===")
tools = {
    "unittest":     "Built-in Python testing framework",
    "pytest":       "Most popular, simple syntax, powerful plugins",
    "httpx":        "Test FastAPI/HTTP endpoints",
    "pytest-mock":  "Mock external dependencies",
    "factory_boy":  "Create test data/fixtures",
    "coverage":     "Measure how much code is tested",
    "locust":       "Load/performance testing",
}
for k, v in tools.items():
    print(f"  {k:16}: {v}")

print("\n=== Testing Pyramid ===")
print("         /\\")
print("        /E2E\\       ← Few, slow, expensive")
print("       /──────\\")
print("      /Integr. \\    ← Some, medium speed")
print("     /──────────\\")
print("    /  Unit Tests \\  ← Many, fast, cheap")
print("   /──────────────\\")

print("\n=== Install ===")
print("  pip install pytest pytest-cov httpx")
print("  Run tests: pytest")
print("  Run with coverage: pytest --cov=. --cov-report=html")
