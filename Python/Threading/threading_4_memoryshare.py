import threading
import time

counter = 0

def increment():
    global counter

    for _ in range(1000):
        current = counter
        time.sleep(0) # time.sleep() --> yield
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

# $ python threading_4_memoryshare.py 
# expected: 2000
# actual: 1123

# $ python threading_4_memoryshare.py 
# expected: 2000
# actual: 1000

# if two threads read the same old value before either writes the updated value,
# one increment can be lost.This is called a race condition

