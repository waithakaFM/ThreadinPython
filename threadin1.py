# Continuation of threading

from threading import Thread, Lock
import time

# define a global variable to simulate the database
database_value = 0


def increase(lock):
    global database_value

    # # the lock prevents another thread from accessing this process at the same time
    # lock.acquire()
    #
    # # get value from database and store it in a local copy
    # local_copy = database_value
    #
    # # processing
    # local_copy += 1
    # # simulate time: processes will take some time
    # time.sleep(0.1)  # time to wait to switch threads
    #
    # # write our new value back to the database
    # database_value = local_copy
    #
    # # release the process
    # lock.release()

    # instead of the above code commented we can use lock as the context manager
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    # to prevent race condition - two or more threads that's wants to modify the same variable

    lock = Lock()
    print('Start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    print("end main")  # when all the processes are done
