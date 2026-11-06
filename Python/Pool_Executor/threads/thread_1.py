from concurrent.futures import ThreadPoolExecutor
import time

def check_service(service_name):
    print(f"Checking {service_name} service...")
    time.sleep(2)  # Simulating network waiting 
    print(f"{service_name} service is healthy.")


services = [
    "Customer API",
    "Payment API",
    "Inventory API",
    "Weather API",
    "Notification API"
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(check_service,services)

    for reseult in results:
        print(reseult)
print("All checks completed")
