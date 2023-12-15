import threading
import random

buf = []
readers_count = 0
write_mutex = threading.Lock()
read_mutex = threading.Lock()
empty = threading.Semaphore(1)
full = threading.Semaphore(0)

def writer():
    global buf
    global write_mutex
    num = random.randint(1, 10)
    empty.acquire()
    write_mutex.acquire()
    buf.append(num)
    print("Produced", num, buf)
    write_mutex.release()
    full.release()

def reader():
    global buf
    global read_mutex
    global readers_count
    read_mutex.acquire()
    readers_count += 1
    if readers_count == 1:
        empty.acquire()
    read_mutex.release()

    full.acquire()
    read_mutex.acquire()

    num = buf.pop(0)
    print("Consumed", num, buf)

    read_mutex.release()

    read_mutex.acquire()
    readers_count -= 1
    if readers_count == 0:
        empty.release()
    read_mutex.release()

writer_thread = threading.Thread(target=writer)
reader_thread = threading.Thread(target=reader)

writer_thread.start()
reader_thread.start()

writer_thread.join()
reader_thread.join()
