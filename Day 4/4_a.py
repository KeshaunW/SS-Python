# Coding Exercise 8

# 1)
def func():
    print('Hello World')


func()
print()


# 2)
def func1(name):
    print('Hi! My name is ' + name)


func1('Google')
print()


# 3)
def func3(x, y, z):
    return x if z else y


print(func3('hello', 'goodbye', False))
print()


# 4)
def func4(x, y):
    return x * y


print(func4(38, 2))
print()


# 5)
def is_even(num):
    return num % 2 == 0


print(is_even(37))
print()


# 6)
def greater_than(a, b):
    return a > b


print(greater_than(74, 2783))
print()


# 7)
def add_all(*nums):
    total = 0
    for i in nums:
        total += i
    return total


print(add_all(48, 584, 5874, 3, 8743, 344))
print()


# 8)
def even_only(*nums):
    answer = ''
    for i in nums:
        answer += str(i) + ' ' if i % 2 == 0 else ''
    return answer


print(even_only(48, 584, 5874, 3, 8743, 344))
print()


# 9)
def weird_case(string):
    temp = ''
    i = 0
    for char in string:
        temp += char.upper() if i % 2 == 0 else char.lower()
        i += 1
    return temp


print(weird_case('Smoothstack'))
print()


# 10)
def which_one(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    else:
        return a if a > b else b


print(which_one(374, 3784))
print()


# 11)
def same_start(a, b):
    return a[0:1] == b[0:1]


print(same_start('Smoothstack', 'Keshaun'))
print()


# 12)
def absolute(a):
    diff = abs(a - 7)
    return 7 + (2 * a) if a < 7 else 7 - (2 * a)


print(absolute(2))
print()


# 13)
def cap(string):
    temp = ''
    i = 0
    for char in string:
        temp += char.upper() if i == 0 or i == 3 else char.lower()
        i += 1
    return temp


print(cap('smoothstack'))
print()
