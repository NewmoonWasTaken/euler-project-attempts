# Find the largest palindrome made from the product of two 3-digit numbers.

# numbers we'll multiply to see if its product is a palindrome
multedone = 999
multedtwo = 999

# product is our answer
# finprod is our candidate for largest
finprod = 0

# unsure a more elegant way so this will be bruteforcy
while multedtwo > 500:
    while multedone > 500:
        # find the product of the two numbers
        product = multedone * multedtwo
        # check if palindrome
        if str(product) == str(product)[::-1] and product > finprod:
            finprod = product
        multedone = multedone - 1
    multedtwo = multedtwo - 1
    multedone = 999

print(finprod)
