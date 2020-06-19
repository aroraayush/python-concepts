from functools import lru_cache

@lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    print(f"Calculating fib {n}")
    return fib(n-1) + fib(n-2)

print("\nfib(10) = ",[fib(x) for x in range(10)])
print("====== fib.cache_info() | <class 'functools.CacheInfo'> ======")
cache_info = fib.cache_info()
print('cache_info.hits: ', cache_info.hits)
print('cache_info.misses: ', cache_info.misses, "\t| Function has to be run for all 10 values atleast once")
print('Hit Ratio : ', round(cache_info.hits / (cache_info.hits + cache_info.misses) * 100,2))
fib.cache_clear()
print("============ fib.cache_clear() ============")
print(fib.cache_info()) # CacheInfo(hits=0, misses=0, maxsize=3, currsize=0)