from multiprocessing import Manager, Pool
from timeit import default_timer
from functools import partial

def mod_test_against_single_prime(prime, multiples, queue):
    # Returns all numbers not divisible by selected prime
    queue.put([x for x in multiples if x % prime])

def main():
    start = default_timer()
    result = sieve(100000)
    print(len(result))
    duration = round(default_timer() - start, 2)
    print(str(duration) + ' seconds')

def sieve(n):
    m = Manager()
    # Using manager to create Queue makes it shared between processes
    q = m.Queue()
    primes = [2]
    # numbers is a little misleading, contains all primes and all possible primes. We remove non-primes below.
    numbers = [2] + list(range(3, n + 1, 2))
    # index used to iterate through the start of the numbers list. As we remove non-primes, that area can only
    # contain primes. [2, 3, 5, 7, 9, ...] -> [2, 3, 5, 7, 11, ...]
    index = 1
    pool = Pool(processes=4)
    to_subtract = []
    while True:
        to_subtract.clear()
        # All multiples of our latest prime, excluding that prime
        primemultiples = list(range(numbers[index] * 2, n, numbers[index]))
        # Feed the worker function some args
        func_plus_data = partial(mod_test_against_single_prime, multiples=primemultiples, queue=q)
        # Do the map, map only takes the arg we iterate through
        pool.map(func_plus_data, primes)
        # Get the non-primes the workers found
        while not q.empty(): to_subtract += q.get()
        done_check = len(numbers)
        numbers = list(set(numbers) - set(to_subtract))
        # Check to see if we actually removed anything, if not, only primes left.
        if not (done_check - len(numbers)): break
        # set subtraction ignores order, need to put order back to use index variable
        numbers.sort()
        # Add latest prime to known primes so we can move to the next
        primes.append(numbers[index])
        index += 1
    pool.close()
    return numbers

if __name__ == '__main__':
    main()