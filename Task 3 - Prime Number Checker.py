def prime_chk(n):
    if n < 2:
        return "The given number is NOT prime"
    
    for i in range(2, n):  # Check divisibility from 2 to n-1
        if n % i == 0:
            return "The given number is NOT prime"
    
    return "The given number is PRIME"

# Taking user input
num = int(input("Enter a number: "))
print(prime_chk(num))
