import threading
import random
import time
import multiprocessing as mp

def generate_random_numbers(number_set, index):
    time.sleep(0.1)
    number_set[index] = [random.randint(0, 10000) for _ in range(100)]

def multithreaded():
    time_taken = []

    for _ in range(10):
        number_sets = [None] * 3

        t1 = threading.Thread(target=generate_random_numbers, args=(number_sets, 0))
        t2 = threading.Thread(target=generate_random_numbers, args=(number_sets, 1))
        t3 = threading.Thread(target=generate_random_numbers, args=(number_sets, 2))

        start_time = time.time_ns()

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

        end_time = time.time_ns()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time)

    return time_taken

def singlethreaded():
    time_taken = []

    for _ in range(10):
        number_sets = [None] * 3
        threads = []

        start_time = time.time_ns()

        for i in range(3):
            generate_random_numbers(number_sets, i)

        end_time = time.time_ns()
        elapsed_time = end_time - start_time
        time_taken.append(elapsed_time)

    return time_taken

def show_result(multithreading_time, non_multithreading_time):
    print("Round-by-Round Performance Comparison")
    print("+-------+--------------------------------+--------------------------------+--------------------------------+")
    print("| Round |    Multithreading Time (ns)    |  Non-Multithreading Time (ns)  |         Difference (ns)        |")
    print("+-------+--------------------------------+--------------------------------+--------------------------------+")
    for index, (multi, non_multi) in enumerate(zip(multithreading_time, non_multithreading_time)):
        diff = multi - non_multi
        print(f"|{index:^7}|{multi:^32}|{non_multi:^32}|{diff:^32}|")
    print("+-------+--------------------------------+--------------------------------+--------------------------------+\n")

    average_multithreading = sum(multithreading_time) // len(multithreading_time)
    average_non_multithreading = sum(non_multithreading_time) // len(non_multithreading_time)

    print("Summary of Result:")
    print("+---------------+---------------------------+---------------------------+--------------------------+")
    print("|     Metric    |    Multithreading (ns)    |  Non-Multithreading (ns)  |      Difference (ns)     |")
    print("+---------------+---------------------------+---------------------------+--------------------------+")
    print(f"|  Total Time   |{sum(multithreading_time):^27}|{sum(non_multithreading_time):^27}|{sum(multithreading_time)-sum(non_multithreading_time):^26}|")
    print(f"| Average Time  |{average_multithreading:^27}|{average_non_multithreading:^27}|{average_multithreading-average_non_multithreading:^26}|")
    print("+---------------+---------------------------+---------------------------+--------------------------+")

if __name__ == "__main__":
    multithreading_time = multithreaded()
    non_multithreading_time = singlethreaded()
    show_result(multithreading_time, non_multithreading_time)