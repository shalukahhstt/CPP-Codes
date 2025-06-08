def factorial(n):
    if n == 0 :
        factorial_n = 1
    elif n > 0 :
        factorial_n = int(n)*int(factorial(n-1))
    return factorial_n

n=int(input("Enter the number: "))
print(factorial(n))