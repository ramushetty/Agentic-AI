import multiprocessing
import time

def process_job():
    print("Child process: job started")
    time.sleep(2)
    print("Child process: job completed")

if __name__ == "__main__":
    # created a process object
    process = multiprocessing.Process(
        target=process_job # specifies the function the child process should execute 
    ) 
    process.start() # starts the child process
    print('Main process: i can continue working')

    process.join() # makes the main process wait until the child finishes

    print("Main process: child has finished")