#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
n = 600851475143
for i in range (2, n+1):
    changed = False
    while n%i == 0:
        n = n/i
        changed = True
    if changed:
        print(i)
