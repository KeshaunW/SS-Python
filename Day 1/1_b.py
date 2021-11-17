# Coding Exercise 2
import math

print('1) Numbers: Example code to add two numbers 50+50 and 100-10 and print it.')
print(50 + 50)
print(100 - 10)
print()

print('2) 30+*6,6^6,6**6,6+6+6+6+6+6')
print(30 + 6 * 6)
print(6 ^ 6)
print(6 ** 6)
print(6 + 6 + 6 + 6 + 6 + 6)
print()

print('3) Print “Hello World” on the console output. Print output “Hello World : 10”')
print('Hello World')
print('Hello World : 10')
print()

print('4) Mathematical Calculation Exercise:')


def payment_calc(p, r, l):
    rate = (r / 12) / 100
    num = (((1 + rate) ** l) - 1)
    denom = (rate * (1 + rate) ** l)
    return math.ceil(p / (num / denom))


print('Input Data:')
userInput = input()
values = userInput.split()
print()

loan = int(values[0])
interest = int(values[1])
months = int(values[2])

print("Answer:")
print(payment_calc(loan, interest, months))
