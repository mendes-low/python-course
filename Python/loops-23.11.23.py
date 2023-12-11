# 1
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1
# else:
#     print(count)

# 2
# count = 1
# while count <= 10:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# 3
# count = 0
# while count <= 8:
#     if count == 5:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# 4
# count = 0
# while count <= 10:
#     if count % 2 == 1:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# 5
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for i in person:
    if i == 'skills':
        for j in person[i]:
            print(j , end=', ')

# for x in person:
#     if x == 'address':
#         for a in person[x]:
#             if a == 'street':
#                 for s in person[a]:
#                     print(s)








