# +1
for i in range(10,21):
    result = i ** 2
    print(result)

# +2
number = int(input("Number:"))
numbers = 0
while number >= 1:
    numbers += number
    number -= 1
print(numbers)

# -3
number = int(input("Number:"))
numbers = 0
while number >= 1:
    numbers = (numbers * number)
    number -= 1
print(numbers)

# +8
number = 20
while number <= 50:
    if number % 3 != 0:
        number += 1
        continue
    if number % 5 == 0:
        number +=1
        continue
    print(number)
    number += 1

# 9
number = 35
while number <= 88:
    if number % 7 == 1:
        number += 1
        continue
    if number % 7 != 0:
        number += 1
        continue
    print(number)
    number += 1 

# 10
number = 1
while number <= 50:
    if number % 5 != 0:
        number += 1
        continue
    if number % 7 != 0:
        number += 1
        continue
    print(number)
    number += 1 


# +11
number = 10
while number <= 99:
    if number % 4 != 0:
        number += 1
        continue
    if number % 6 == 0:
        number +=1
        continue
    print(number)
    number += 1

# 12
number = 10
numbers = 0
while number <= 99:
    if number % 2 == 0:
        number += 1
    if number % 13 == 0:
        number += 1
        continue
    print(number)
    number += 1


# +14
number = int(input("Number:"))
for i in range(1,number+1):
    result = i ** 2
    print(result)
