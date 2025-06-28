import time
from threading import Thread

def countdown(n):
    while n > 0:
        n -= 1
        # time.sleep(0.00001)

def single_thread(n):
    start = time.time_ns()
    countdown(n)
    end = time.time_ns()
    print("Time taken in single thread (ns): ", end - start)

def multithread(n):
    start = time.time_ns()

    #split the task between two thread
    t1 = Thread(target=countdown, args=(n//2,)) #comma is needed as args is a tuple
    t2 = Thread(target=countdown, args=(n//2,))

    # start executing the countdown function
    t1.start()
    t2.start()

    # wait for the threads to finish before moving on
    t1.join()
    t2.join()

    end = time.time_ns()
    print("Time taken in multi-thread (ns): ", end - start)

if __name__ == "__main__":
    count = 1000
    single_thread(count)
    multithread(count)