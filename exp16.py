import math

n = int(input("Enter number of terms: "))

phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2

print("Fibonacci Series:")

for i in range(n):
    fib = round((phi**i - psi**i) / math.sqrt(5))
    print(fib, end=" ")