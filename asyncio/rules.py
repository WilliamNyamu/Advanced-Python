# import asyncio

# async def f(x):
#     y = await z(x)  # Okay - `await` and `return` allowed in coroutines
#     return y

# async def g(x):
#     yield x  # Okay - this is an async generator

# async def m(x):
#     yield from gen(x)  # No - SyntaxError

# def n(x):
#     y = await z(x)  # No - SyntaxError (no `async def` here)
#     return y
