# Find the sum of all the multiples of 3 or 5 below 1000

# something is a multiple of 5 if it end in 5 or 0
# something is a multiple of 3 if its digits add up to 3 but idk how to code that
# there are overlaps, too!

# variable to keep track of how high up we're going
# 1 and 2 won't be there so i'll save time
count = 3

# our final result we cumulatively add to
total = 0

while count < 1000:
    print("checking " + str(count))
    
    # check if it's divisible by 5 by checking the last digit
    # while also checking if it's divisible by 3 in the same step to save lines
    if str(count)[-1] == "5" or str(count)[-1] == "0" or count % 3 == 0:
        total = total + count
        print("divisible, new total is " + str(total))

    # advance the counter
    count = count + 1

# get our final result
print("counter stopping, total is " + str(total))
