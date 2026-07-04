# GraphQL Subscriptions - Real-time data via WebSocket
# pip install strawberry-graphql[fastapi] uvicorn
# Run: uvicorn subscriptions:app --reload

import strawberry
import asyncio
from typing import AsyncGenerator, List, Optional
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# --- Types ---
@strawberry.type
class Message:
    id: int
    user: str
    text: str

@strawberry.type
class Notification:
    type: str
    message: str
    user_id: int

# --- In-memory message store ---
messages = []
msg_id = 1

# --- Query ---
@strawberry.type
class Query:
    @strawberry.field
    def messages(self) -> List[Message]:
        return messages

# --- Mutation ---
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_message(self, user: str, text: str) -> Message:
        global msg_id
        msg = Message(id=msg_id, user=user, text=text)
        messages.append(msg)
        msg_id += 1
        return msg

# --- Subscription ---
@strawberry.type
class Subscription:

    @strawberry.subscription
    async def count(self, target: int = 10) -> AsyncGenerator[int, None]:
        for i in range(1, target + 1):
            yield i
            await asyncio.sleep(1)

    @strawberry.subscription
    async def live_notifications(self, user_id: int) -> AsyncGenerator[Notification, None]:
        events = [
            Notification(type="order", message="Your order shipped!", user_id=user_id),
            Notification(type="promo", message="50% off today!", user_id=user_id),
            Notification(type="alert", message="Login from new device", user_id=user_id),
        ]
        for event in events:
            yield event
            await asyncio.sleep(2)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print("=== Example Subscriptions (run in GraphiQL at /graphql) ===")
print("""
# Count subscription (streams 1 to 5)
subscription {
  count(target: 5)
}

# Live notifications
subscription {
  liveNotifications(userId: 1) {
    type
    message
  }
}
""")

print("=== How Subscriptions Work ===")
print("  1. Client connects via WebSocket to /graphql")
print("  2. Client sends subscription query")
print("  3. Server streams data as events happen")
print("  4. Client receives updates in real-time")
print("  5. Client can unsubscribe anytime")
