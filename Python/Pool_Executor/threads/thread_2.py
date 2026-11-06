# future - current status of task

from concurrent.futures import ThreadPoolExecutor
import time

def check_service(service_name):
    print(f"Checking {service_name} service...")
    time.sleep(2)  # Simulating network waiting 
    print(f"{service_name} service is healthy.")



with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(check_service,"Customer API")

    print("The job has been submitted")
    # future.done() helps to check the status and return True if job is finished
    print("Is it finished? ", future.done())

    result = future.result()
    print("Result: ", result)
print("All checks completed")
