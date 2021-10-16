sum = 0 

a = 1 
b = 2

while b <= 4000000:
    if b%2 == 0:
        sum+= b
    c = b
    b = b + a
    a = c 
    

print(sum)