# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

total = 1

for i in range(1, 21):
    if total % i != 0:
        should_skip = False
        for j in range (2, int(i/2)+1):
            if i % j == 0:
                total *= j
                should_skip = True
                break
        if should_skip:
            continue
        total*=i

print(total)
