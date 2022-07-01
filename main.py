# multithreading

from threading import Thread
import os
import time


# function executed by the threads
def square_numbers():
    for i in range(100):
        i = i
        time.sleep(0.1)


threads = []
num_threads = 10


for i in range(num_threads):
    t = Thread(target=square_numbers)  # if our function has an argument we specify them after target using args=(
    # arguments)
    threads.append(t)

# start the threads
for t in threads:
    t.start()

# join thread: wait for them to complete
for t in threads:
    t.join()

print("end main")  # when all the processes are done