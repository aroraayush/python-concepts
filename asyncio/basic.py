import asyncio

# Related Concepts
# Concurrency: encompasses both
#         1. multiprocessing (ideal for CPU-bound tasks) 
#         2. threading (suited for IO-bound tasks)

# 1. Multiprocessing : means to effect parallelism
#     1.a) Parallelism : consists of performing multiple operations at the same time  
# - Multiprocessing entails spreading tasks over a computer’s CPUs, or cores

# 2. Threading: better for IO-bound tasks
#   - Concurrent execution model whereby multiple threads take turns executing tasks.

# asyncio
# async IO is a style of concurrent programming, but it is not parallelism.
# Concurrency - Parallelism => (Threading + Parallelism) - Parallelism = Threading
# async IO is a single-threaded, single-process design: it uses cooperative multitasking

# Use async IO when you can; use threading when you must
#       Async IO avoids some of the potential speedbumps that 
#       you might otherwise encounter with a threaded design

# async/await: two new Python keywords that are used to define coroutines
# asyncio: the Python package that provides API for running and managing coroutines

def f():
    pass

async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r

print("=========== Without asyncio (3 seconds) ===============")
import time

def count_without_async():
    print("One")
    time.sleep(1)
    print("Two")

def main_without_async():
    for _ in range(3):
        count_without_async()

s = time.perf_counter()
main_without_async()
elapsed = time.perf_counter() - s
print(f"main_without_async() executed in {elapsed:0.2f} seconds.")


print("=========== With asyncio (1 second) ===============")
async def count_with_async():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main_with_async():
    await asyncio.gather(count_with_async(), count_with_async(), count_with_async())


s = time.perf_counter()
asyncio.run(main_with_async())
elapsed = time.perf_counter() - s
print(f"main_with_async() executed in {elapsed:0.2f} seconds.")

