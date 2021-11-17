# Coding Exercise 6

def crowd_check(lst):
    if len(lst) > 5:
        print('Feels like a mob in here...')
    elif 3 <= len(lst) <= 5:
        print('This room is crowded...')
    else:
        print('This isn\'t so crowded...')


people = ['Adam', 'Jenny', 'Susan', 'William', 'Jim', 'Barbara', 'Alex', 'Jessie']
crowd_check(people)

while len(people) > 5:
    people.pop(0)

crowd_check(people)

while len(people) >= 3:
    people.pop(0)

crowd_check(people)
