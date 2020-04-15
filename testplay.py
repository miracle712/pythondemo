import _thread
import time

def print_thread( ThreadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( ThreadName,time.ctime(time.time())))
try:
    _thread.start_new_thread( print_thread, ("Thread-1",2,))
    _thread.start_new_thread( print_thread, ("Thread-2",2,))
except:
    print("Error:无法启动线程")

while 1:
    pass