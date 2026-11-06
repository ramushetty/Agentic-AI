from concurrent.futures import ProcessPoolExecutor
import time 

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2,int(number ** 0.5)+1):
        if number % divisor == 0:
            return False 
    return True

def count_primes(start,end):
    return sum(
        1 for number in range(start,end)
        if is_prime(number)
    )

if __name__ == "__main__":
    ranges = [
        (2,50_000),
        (50_000, 100_000),
        (100_000,150_000),
        (150_000, 200_000)
    ]

    start_time = time.perf_counter

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(count_primes,start,end)
            for start,end in ranges
        ]

        results = [future.result() for future in futures]

        print("Counts: ", results)
        print("Total Primes: ", sum(results))
        print(f"Elapsed time: {time.perf_counter() - start_time:.2f} seconds" )

