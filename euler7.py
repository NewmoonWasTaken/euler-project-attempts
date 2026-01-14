# what is the 10001st prime number?

import math

def isPrime(num):
    res = True
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0:
            res = False
            break
    return res

counter = 1
num = 3

while counter < 10001:
    if isPrime(num) == True:
        counter = counter + 1
    num = num + 2

print(str(num - 2))
