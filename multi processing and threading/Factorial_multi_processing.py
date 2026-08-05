import multiprocessing
import math
import sys
import time


## incease the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number

def computer_factorial(number):
    print(f"computing factoral of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result


if __name__=="__main__":
    numbers=[5000,6000,7000,8000]

    start_time=time.time()

## crate a pool of worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"time taken: {end_time - start_time }")
