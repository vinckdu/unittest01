import _thread
import time


def print_time(thread_name, delay):
    count = 0
    while count < 100:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("thread01", 2))
    _thread.start_new_thread(print_time, ("thread01", 2))
except Exception as e:
    print("Error,can't start the threading")
    print(e)

while 1:
    pass










