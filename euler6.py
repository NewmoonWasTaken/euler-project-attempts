# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sm = 0
sqr = 0

for i in range(1,101):
    sm = sm + i
sm = sm * sm
print(sm)

for i in range(1,101):
    sqr = sqr + (i * i)
print(sqr)

print(sqr - sm)
