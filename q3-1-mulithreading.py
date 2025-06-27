import time
from threading import Thread

def countdown(n):
    while n > 0:
        n -= 1

def single_thread(n):
    start = time.time()
    countdown(n)
    end = time.time()
    print("Time taken in single thread (s): ", end - start)

def multithread(n):
    start = time.time()

    #split the task between two thread
    t1 = Thread(target=countdown, args=(n//2,)) #comma is needed as args is a tuple
    t2 = Thread(target=countdown, args=(n//2,))

    # start executing the countdown function
    t1.start()
    t2.start()

    # wait for the threads to finish before moving on
    t1.join()
    t2.join()

    end = time.time()
    print("Time taken in multi-thread (s): ", end - start)

if __name__ == "__main__":
    count = 5000000
    single_thread(count) # Time taken in single thread (s):  0.15227031707763672
    multithread(count) # Time taken in multi-thread (s):  0.15409135818481445