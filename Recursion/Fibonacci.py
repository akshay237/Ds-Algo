def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter the number till which fibonacci series is found:\n"))
print("Fibonacci series till ", num, "is: ")
for i in range(num):
    print(fibonacci(i))