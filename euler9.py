# there exists exactly one Pythagorean triplet for which a+b+c=1000. find the product a*b*c

# a + b + sqrt(a*a+b*b) = 1000

for a in range(1,500):
    for b in range(1,500):
        c = 1000-a-b
        if a*a + b*b == c*c:
            print(str(a*b*c))
            quit()
