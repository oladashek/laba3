import random
p = 0
n = 0
while n < 3:
    num = str(random.randint(1, 10))
    num1 = str(random.randint(1, 10))
    s = str(input("решите!!!!!"+ num + " + " + num1 + " = "))
    if int(s) == int(num) + int(num1):
        print("правильно!!!")
        p += 1
    else:
        print("неправильно!!!")
        n += 1
print("конец!   правильных ответов : " + str(p) )

