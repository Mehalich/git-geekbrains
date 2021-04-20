#1
a = 1
b = "Миша"
c = True
name = input("Введите ваше имя: ")
d = int(input("Сколько вам лет? "))
print("a =", a, ",b =", b, ",c =", c)
print("Зовут вас ", name, " и вам ", d, "лет")
#2
sec = int(input("введите пожалуйста кол-во секунд: "))
ho = (sec // (60*60))
mi = (sec // 60 % 60)
se = (sec % 60)
print (f"{ho}:{mi}:{se}")
#3
n = input("введите число: ")
nn = n + n
nnn = n + n + n
print(int(n) + int(nn) + int(nnn))
#4
m = 0
n = input("введитев целое положительное число: ")
big = n[0]
while m < len(n):
    if n[m] > big:
        big = n[m]
    m = m + 1
print("самое большая цифра в числе: ", big)
#5
revenue = int(input("введите значение выручки фирмы: "))
cost = int(input("введите значение издержек фирмы: "))
if revenue < cost:
    print("Финансовые показатели такие себе, вы работаете в убыток")
elif revenue == cost:
    print("Финансовые показатели такие себе, вы работаете в ноль")
else:
    print("Финансовые показатели в порядке, вы работаете в прибыль")
    profit = revenue - cost
    profitability = revenue / cost
    quantity = int(input("Введите кол-во сотрудников: "))
    print(f"прибыль фирмы: {profit}")
    print(f"рентабельность выручки: {profitability}")
    print(f"прибыль фирмы в расчете на одного сотрудника: {profit / quantity}")
#6
a = int(input("Введите результат первого дня (больше нуля): "))
b = int(input("Введите, сколько км хотелось бы: "))
day = 1
while a < b:
    print(f"{day}-й день:{round(a, 2)}")
    a = a + (a / 10)
    day += 1
print(f"{day}-й день: {round(a, 2)}")
print(f"на {day}-й день спортсмен достиг результата не менее {b} км.")