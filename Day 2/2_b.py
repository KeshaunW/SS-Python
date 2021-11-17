# Coding Exercise 4

list1 = [12, 'December', '6.3']
print('1) ' + str(list1))
print()

# The provided nested list ([1,1[1,2]]) is incorrect.
# The following assumes the nested list is intended to be [1,1,[1,2]]
nested = [1, 1, [1, 2]]
print('2) ' + str(nested[2][1]))
print()

list2 = ['a', 'b', 'c']
print('3) ' + str(list2[1:]))
print()

dotw = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
print('4) ' + str(dotw))
print()

d = {'k1': [1, 2, 3]}
print('5) ' + str(d['k1'][1]))
print()

list3 = [1, [2, 3]]
tuple1 = tuple(list3)
print('6) ' + str(tuple1))
print()

set1 = set('Mississippi')
print('7) ' + str(set1))
print()

set1.add('X')
print('8) ' + str(set1))
print()

set2 = {1, 1, 2, 3}
print('9) ' + str(set2))
print()

answer = []
for num in range(2000, 3200):
    if num % 7 == 0 and num % 5 != 0:
        answer.append(str(num))
print('Question 1: ' + ','.join(answer))
print()

print('Question 2:')
value = int(input())
product = 1
while value > 0:
    product *= value
    value -= 1
if value < 0:
    product = 'N/a'
print(product)
print()

print('Question 3:')
value = int(input())
dict1 = {}
i = 1
for i in range(1, value + 1):
    dict1[i] = i**2
print(dict1)
print()

print('Question 4:')
list3 = input().split(',')
tuple2 = tuple(list3)
print(list3)
print(tuple2)

print('Question 5:')


class StringsAreFun:
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


fun = StringsAreFun()
fun.getString()
fun.printString()
print()
