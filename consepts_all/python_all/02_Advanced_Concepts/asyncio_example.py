import asyncio


async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello {name}")


async def main():
    await asyncio.gather(greet("Ajay"), greet("Ravi"))


asyncio.run(main())
