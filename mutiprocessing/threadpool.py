from functools import partial
from multiprocessing import Pool, Manager, Lock

def target(lock, items):
    print("items", items)
    for item in items:
        lock.acquire()
        print("item", item)
        lock.release()
        
def main():
    iterable = [1, 2, 3, 4, 5]
    pool = Pool(5)
    m = Manager()
    l = m.Lock()
    func = partial(target, l)
    pool.map(func, iterable)
    pool.close()
    pool.join()

if __file__ == "__main__":
    main()