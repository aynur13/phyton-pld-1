y = int(input())
s = 0
if y == 1:
    print(y,"is not prime and prime")
else:
    for i in range (2, int(y**(0.5) + 1)):
        if y % i == 0:
            s = s+1
    if (s > 0):
        print(y, "is not prime")
    else:
        print(y, "is prime")
