# Coding Exercise 3

print('1) ' + 'Hello World'[-3])
print()

print('2) ' + 'thinker'[2:-2])
print()

s = 'Sammy'
print('3) ' + s[2:])
print()

print('4) ', end='')
print(set('Mississippi'))
print()

print()
print('Input Data:')

while True:
    userInput = input()
    if userInput.isnumeric():
        break

i = 0
answer = ''
while i < int(userInput):
    arg = input()
    checking = ''
    for letter in arg:
        checking += letter if letter.isalnum() else ''
    checking = checking.lower()
    answer += 'Y ' if checking == checking[::-1] else 'N '
    i += 1

print()

print("Answer:")
print(answer)

#answer = ''
#for arg in args:
#    checking = ''
#    for letter in arg:
#        checking += letter if letter.isalnum() else ''
#    answer += 'Y ' if checking == checking[::-1] else 'N '

