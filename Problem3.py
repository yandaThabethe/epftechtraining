n = 600851475143
i = 2           #we're using 2 because it's the smallest prime number
while n != 1:
    rem = n%i   
    if rem == 0:
        n = n/i
        print(i)
    else:
        i +=1