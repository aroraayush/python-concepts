# Multiprocessing is used to spawm multiple child
# Used for Concurrent Programming
# Uses Global interpreter lock (GIL)

# Using all the processors on our machine

import os
from multiprocessing import Process, current_process

def square(num):
    res = num * num
    process_id = os.getpid()
    # Processes declared sequentiall for our own working
    py_process_name = current_process().name
    print(f"{py_process_name}. The number {num} squares to {res} \t| ran on process_id {process_id}")

if __name__ == '__main__':

    numbers = [1, 2, 3, 4]
    numbers = range(100)
    processes = []

    for num in numbers:
        process = Process(target=square, args=(num,))
        processes.append(process)

        # Processes will be spawned with the process object
        process.start()