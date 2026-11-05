import threading
import time

# threading lib uses time slicing to switch between threads and it is not true parallelism.

def check_service(service_name):
    print(f"Checking {service_name} service...")
    time.sleep(2)  # Simulating a blocking operation
    print(f"{service_name} service is running.")
# thread object
thread = threading.Thread(
    target=check_service,
    args=("Customer Database",))
#start thread
thread.start()

# thread.join() # Wait for the thread to finish

print("monitoring service check completed.")

'''
1. Main thread creates a new thread
2. start() allows the new thread to execute check_service function
3. the new thread prints the first message and sleeps for 2 seconds
4. meanwhile new thread reaches the joins() and waits for the new thread to finish
5. after 2 seconds the new thread prints the second message and finishes execution
6. join() returns and the main thread continues execution and prints the last message
'''