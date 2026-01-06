# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# by this we track how far along the sequence we are
cur = 1
# temporary previous number for processing
temprev = 0
# previous number
prev = 1
# output
total = 0

while cur < 4000000:
    # add current number to the total only if divis by 2
    if cur % 2 == 0:
        total = total + cur
    # set our temporary value to be the previous value
    temprev = prev
    # advance prev
    prev = cur
    # advance cur
    cur = cur + temprev
    # to ensure this is still working
    print(cur)

# supply final answer
print("breaking loop, total is:")
print(total)
