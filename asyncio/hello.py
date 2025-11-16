import asyncio

async def greet(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    print("Hoow you doing?")

asyncio.run(greet("William"))