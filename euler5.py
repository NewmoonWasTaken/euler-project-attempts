# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# our starting guess
# we'll go in increments of 20 to save time
total = 2520

# we only need to check for 19, 18, 17, 16, 15, 14, 13, 12, 11

while True:
    done = True
    for i in range (11, 20):
        if total % i != 0:
            done = False
            break
    if done == True:
        print(total)
        print("^ final")
        quit()
    else:
        total = total + 20
