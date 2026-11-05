import threading
import time

def check_service(service_name):
    print(f"Checking {service_name} service...")
    time.sleep(2)  # Simulating a blocking operation
    print(f"{service_name} service is running.")

start = time.perf_counter()

threads = []
services = ["Customer Database", "Weather API", "AI Inference Service"]
for service in services:
    thread = threading.Thread(target=check_service, args=(service,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

end = time.perf_counter()

print(f"Total time taken: {end - start} seconds")

print("monitoring service check completed.")

# $ python threading_3.py 
# Checking Customer Database service...
# Checking Weather API service...
# Checking AI Inference Service service...
# Customer Database service is running.
# AI Inference Service service is running.
# Weather API service is running.
# Total time taken: 2.002373799914494 seconds
# monitoring service check completed.