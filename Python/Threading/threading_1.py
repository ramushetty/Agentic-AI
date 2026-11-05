# we are building a company monitoring service 
# a customer database
# an external weather API
# an ai inference  service

# python by default is sequential 

import time 

def read_customer():
    print("Reading customer data from database...")
    time.sleep(2) #blocking
    print("Customer data read successfully.")

def fetch_weather():
    print("Fetching weather data from external API...")
    time.sleep(3)
    print("Weather data fetched successfully.")

def run_prediction():
    print("Running AI inference service...")
    time.sleep(4)
    print("AI inference completed successfully.")

start = time.perf_counter()

read_customer()
fetch_weather()
run_prediction()

end = time.perf_counter()

# total took 9 seconds to run all the tasks sequentially.
print(f"Total time taken: {end - start} seconds")