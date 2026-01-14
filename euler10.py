# find the sum of all the primes below two million

import math

def isPrime(num):
    res = True
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0:
            res = False
            break
    return res

total = 0

for i in range(2,2000000):
    if isPrime(i) == True:
        total = total + i

print(total)
