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

