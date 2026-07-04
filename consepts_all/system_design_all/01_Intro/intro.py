# System Design - Design large-scale systems
# Most asked in senior developer and architect interviews

print("=== What is System Design? ===")
print("  How to design systems that handle millions of users")
print("  Focus: scalability, reliability, availability, performance\n")

print("=== Key Concepts ===")
concepts = {
    "Scalability":      "Handle more users/data by adding resources",
    "Availability":     "System is up and working (99.9% = 8.7 hrs downtime/year)",
    "Reliability":      "System works correctly even when parts fail",
    "Latency":          "Time to respond to one request (ms)",
    "Throughput":       "Requests handled per second (RPS)",
    "Consistency":      "All users see same data at same time",
    "Partition":        "System works even if network splits",
    "CAP Theorem":      "Can only guarantee 2 of: Consistency, Availability, Partition",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== Horizontal vs Vertical Scaling ===")
print("  Vertical (Scale Up):   Add more CPU/RAM to same server — limited, expensive")
print("  Horizontal (Scale Out): Add more servers — unlimited, needs load balancer\n")

print("=== System Design Interview Steps ===")
steps = [
    "1. Clarify requirements (functional + non-functional)",
    "2. Estimate scale (users, requests/sec, data size)",
    "3. Define API endpoints",
    "4. Design high-level architecture (draw boxes)",
    "5. Design database schema",
    "6. Identify bottlenecks and add caching/queues",
    "7. Discuss trade-offs",
]
for s in steps:
    print(f"  {s}")

print("\n=== Common System Design Topics ===")
topics = [
    "URL Shortener (bit.ly)",
    "Chat System (WhatsApp)",
    "News Feed (Twitter/Instagram)",
    "Video Streaming (YouTube/Netflix)",
    "Ride Sharing (Uber)",
    "Search Autocomplete (Google)",
    "Rate Limiter",
    "Distributed Cache",
]
for t in topics:
    print(f"  - {t}")
