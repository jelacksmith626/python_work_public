import string, random

people = []
get_people = input('Who do you want to add (print "done" when done): ')
people.append(get_people)
while get_people != 'done':
    get_people = input('Who do you want to add (print "done" when done): ')
    people.append(get_people)
    get_people = get_people.lower()
if get_people == 'done':
    people.remove('done')
person = random.choice(people)
print(f'I think it should be {person.upper()}')

    
    