# Coding Exercise 7
import random

answer = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        answer.append(num)

print('1) ' + str(answer))
print()


def convert(**degree):
    if 'fahrenheit' and 'celsius' in degree:
        print('Select one to convert from, not both')
    elif 'fahrenheit' in degree:
        celsius = (5 * (degree['fahrenheit'] - 32)) / 9
        print("{degree['fahrenheit']} F is {celsius} in Celsius")
    elif 'celsius' in degree:
        fahrenheit = (9 * (degree['celsius'] / 5)) + 32
        print("{degree['celsius']} C is {fahrenheit} in Fahrenheit")
    else:
        print('Select one to convert from')


print('2) ', end='')
convert(celsius=25)
print()

num = random.randint(1, 9)
print('3) Guess a number between 1 and 9.')

while True:
    guess = int(input())
    if (guess == num):
        print('You guessed correctly!')
        break
    else:
        print('You guessed incorrectly. Try again!')
print()

print('4)')
for i in range(1, 6):
    print('*' * i)
    if i == 5:
        for j in range(4, 0, -1):
            print('*' * j)
print()

word = str(input('6) Enter a word you would like to be reversed: '))
print(word[::-1])
print()

def checkEvenOdd(numbers):
    evenodd = {
        'even': 0,
        'odd': 0
    }
    for number in numbers:
        if number % 2 == 0:
            evenodd['even'] += 1
        else:
            evenodd['odd'] += 1
    return evenodd


print('7)')
values = checkEvenOdd((1, 2, 3, 4, 5, 6, 7, 8, 9))
print('Number of Even Numbers: ' + str(values['even']))
print('Number of Odd Numbers: ' + str(values['odd']))
print()

print('8)')
args = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for arg in args:
    print(str(arg) + ' ' + str(type(arg)))
print()

allnum = ''
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    allnum += ' ' + str(i)
print('9)' + allnum)
