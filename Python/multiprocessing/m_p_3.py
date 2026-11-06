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

if __name__ == "__main__":
    start_time = time.perf_counter()

    total = count_primes(2,200_000)

    elapsed = time.perf_counter() - start_time

    print("Prime count:",total)
    print(f"Sequential time: {elapsed:.2f} seconds")

# $ python m_p_3.py 
# Prime count: 17984
# Sequential time: 0.34 seconds