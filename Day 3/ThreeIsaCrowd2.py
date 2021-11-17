# Coding Exercise 6

def crowd_check(lst):
    if len(lst) >= 3:
        print('This room is crowded...')
    else:
        print('This isn\'t so crowded...')


people = ['Adam', 'Jenny', 'Susan', 'William', 'Jim']
crowd_check(people)

while len(people) >= 3:
    people.pop(0)

crowd_check(people)
