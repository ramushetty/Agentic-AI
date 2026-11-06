import multiprocessing
import time 

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2,int(number ** 0.5)+1):
        if number % divisor == 0:
            return False 
    return True

def count_primes(start,end):
    count =0
    for number in range(start,end):
        if is_prime(number):
            count+=1
    return count

def worker(start,end,result_queue):
    result = count_primes(start,end)
    result_queue.put(result)

if __name__ == "__main__":
    ranges = [
        (2,50_000),
        (50_000, 100_000),
        (100_000,150_000),
        (150_000, 200_000)
    ]
    result_queue = multiprocessing.Queue()
    processes = []

    start_time = time.perf_counter()

    for start, end in ranges:
        process = multiprocessing.Process(
            target=worker,
            args=(start,end,result_queue)
        )
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    total = sum(result_queue.get() for _ in processes)

    elapsed = time.perf_counter() - start_time
    print("Prime count:",total)
    print(f"multiprocessing time: {elapsed:.2f} seconds")

# $ python m_p_4.py 
# Prime count: 17984
# multiprocessing time: 0.27 seconds