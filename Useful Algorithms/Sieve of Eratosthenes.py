from timeit import default_timer
# algorithm to find all prime numbers under a given number
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve_of_eratosthenes(n):
    numbers = [2] + list(range(3, n + 1, 2))
    primes = [2]
    count = 1
    while True:
        nonduplicates = []
        primemultiples = list(range(numbers[count] * 2, numbers[-1] + 1, numbers[count]))
        for x in primemultiples:
            if all(map(lambda y: x % y != 0, primes)): nonduplicates.append(x)
        if not nonduplicates: break
        primes.append(numbers[count])
        numbers = list(set(numbers) - set(nonduplicates))
        numbers.sort()
        count += 1
    print(numbers[-1])
    return numbers

start = default_timer()
print(len(sieve_of_eratosthenes(1000000)))
duration = round(default_timer() - start, 2)
print(str(duration) + ' seconds')