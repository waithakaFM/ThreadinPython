# Continuation of threading
# use of queue(FIFO) which are excellent for thread save and data save

from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
    while True:
        value = q.get()

        # processing..
        with lock:
            print(f'in {current_thread().name} got {value}')
            q.task_done()


if __name__ == "__main__":
    # # using queues
    # q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # # 3 2 1 -->
    # # get and remove first item
    # first = q.get()
    # print(first)
    # # check if the queue is empty
    # print(q.empty())
    # q.task_done() # tell the program we are done processing this process
    # q.join()  # this block the main process and wait until the other processes are done

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # deamon thread is a background thread that will die when the main thread die
        thread.start()

    # fill our queue with elements
    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")
