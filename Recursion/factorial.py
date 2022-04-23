def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter a number:\n"))
res = fact(num)
print("Factorial of ", num, " is: ", res)