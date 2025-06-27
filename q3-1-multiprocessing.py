import time
from multiprocessing import Pool

def countdown(n):
    while n > 0:
        n -= 1

def multiprocessing(n):
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [n//2])
    r2 = pool.apply_async(countdown, [n//2])
    pool.close
    pool.join
    end = time.time()
    print("Time taken to run in multiprocessing (s):", end - start)

if __name__ == "__main__":
    count = 5000000
    multiprocessing(count)