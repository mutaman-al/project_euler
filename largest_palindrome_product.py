# A palindromic number reads the same both ways. The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(number):
    number = str(number)

    for i in range (0, int(len(number)/2)):
        if number[i] != number[0-i-1]:
            return False
    
    return True

for i in range(998002):
    if is_palindrome(998002-i):
        factor = 0
        should_leave = False

        for j in range(999):
            if (998002-i) % (999-j) == 0:
                factor = 999 - j
                if factor > 99 and factor < 1000 and (998002-i)/factor > 99 and (998002-i)/factor < 1000:
                    print(998002-i)
                    print(factor)
                    print((998002-i)/factor)
                    should_leave = True
                    break

        if should_leave:
            break




