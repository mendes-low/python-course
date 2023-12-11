person = {
    'first_name':'Aziz',
    'last':'Uskembaev',
    'age':16,
    'country':'Kazakhstan',
    'city':'Almaty',
    'color':'black',
    'I\'m  clever':True,
    'skills':['HTML' , 'CSS' , 'JS' , 'Python'],
    'language':{'Kazakh' , 'Rissian' , 'English' , 'English'},
    'addrees':('Almaty Arena')
}
print(person)

person['fruits'] = ['mango' , 'apple' , 'cherry'] 
print(person)

person['age'] += 1
print(person)

person['skills'].append('Java')
print(person)

print(person.get('country'))

print('favorite_subject' in person)

print(person.items())

print(person.clear())

del person

keys = person.keys()
print(keys)

value = person










