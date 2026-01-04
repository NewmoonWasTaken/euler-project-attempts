# euler problem 0!
# Among the first 303 thousand square numbers, what is the sum of all the odd squares?

# an odd number squared is odd also
# an even number squared is even also
# so i need to add up the odd squares from 0 to 303000

# total will be the final answer that i add to
total = 0

# squared will be the number i square
squared = 1

while squared < 303000:
    print("still working, up to " + str(squared))
    
    # find the square of current number
    square = squared * squared

    # add this to the total
    total = total + square

    # update for new square
    squared = squared + 2

# then print the result
print("so the total is " + str(total))
