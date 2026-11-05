# threading.Lock()
import threading
import time

counter = 0
counter_lock = threading.Lock()

def increment():
    global counter

    for _ in range(1000):
        with counter_lock:
            current = counter
            time.sleep(0)
            counter = current+1
        
threads = [
    threading.Thread(target=increment),
    threading.Thread(target=increment)
 ]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print('expected:',2000)
print("actual:", counter)


# $ python threading_using_lock_5.py 
# expected: 2000
# actual: 2000

# $ python threading_using_lock_5.py 
# expected: 2000
# actual: 2000