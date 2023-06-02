sum = 1
n1 = 1
n2 = 0
fnum = 0

while fnum <4000000:
    
    n1 = n2
    n2 = sum
    sum = n1 + n2
    #print(sum)

    if sum%2 == 0:
        fnum = fnum + sum

print(fnum)