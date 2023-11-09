#1
# import random
# choice =  input("Choice?")
# choices = ["rock", "paper", "scissors"]
# computer_choice = random.choice(choices)
# print(computer_choice)

#2
# word = "dark"
# answer = input("Угадай слова:") 
# if answer == word:
#     print("Ты угадал слова!")
# else:
#     print("Ты не угадал слова!")

#3
# number = int(input("Скажите мне первое числа:"))
# number2 = int(input("Скажите мне второе числа:"))
# oper = input("Выбери оператора:")
# if oper == "+":
#     print(number + number2)
# elif oper == "-":
#     print(number - number2)
# elif oper == "*":
#     print(number * number2)
# elif oper == "/":
#     print(number / number2)

#4
# print("Можно ли купить вино?")
# wine = int(input("Хорошо,сколько вам лет?"))
# if wine < 21:
#     print("Простите мы не можем продать вам вино")
# else:
#     print("Хорошо,вот ваше вино")

# 5
# ticket = int(input("Сколько вам лет?"))
# if ticket < 18:
#     print("Тогда вам десткий билет")
# elif ticket < 50:
#     print("Тогда вам взрослый билет")
# else:
#     print("Тогда вам пожилой билет")
# price = input("Значит вам...")
# if price == "десткий":
#     print("С вас 1000")
# elif price == "взрослый":
#     print("С вас 1500")
# else:
#     print("С вас 500")

#6
# string = input("Напиши слова полидром:")
# if string == string[::-1]:
#     print("Это полидром")
# else:
#     print("Это не полидром")

#7
# credit = int(input("Сумма кредита?"))
# persent = int(input("Процент кредита?"))
# term = int(input("Срок в месяцах?"))
# persent2 = persent / ( 100 / 12 )
# monthly_payment = credit * (persent2 + ((persent2 / persent2) * term))
# print(persent2)
# print(monthly_payment) 

#8
# number = int(input("Напишите число:"))
# if number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print("Fizzbuzz")

#9
# grade = int(input("Оценка 1 теста:"))
# grade2 = int(input("Оценка 2 теста:"))
# grade3 =int(input("Оценка 3 теста:"))
# total = (grade + grade2 + grade3) // 3
# if total >= 80:
#     print("A")
# elif total >= 70:
#     print("B")
# elif total >= 60:
#     print("C")
# elif total >= 50:
#     print("D")
# else:
#     print("F")

#10
# kg = int(input("Масса тело:"))
# height = float(input("Рост кавадрат метрах:"))
# height2 = height * height 
# BMI = kg // height2
# if BMI <= 18:
#     print("у вас дефицит массы")
# elif BMI >= 18:
#     print("У вас нет избыточного веса")
# elif BMI >= 25:
#     print("У вас избыточная масса")
# elif BMI >= 30:
#     print("У вас ожирение 1 степени")
# elif BMI >= 35:
#     print("У вас ожирение 2 степени")
# elif BMI >= 40:
#     print("У вас ожирение 3 степени")
# else:
#     print("У вас ожирение 4 степени")


