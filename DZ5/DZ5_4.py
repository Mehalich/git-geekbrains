"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open("DZ5_4.txt") as f:
    lines = f.readlines()
f_new = open("DZ5_4_new.txt", "w")
for line in lines:
    if "One" in line:
        line = line.replace("One", "Один")
    elif "Two" in line:
        line = line.replace("Two", "Два")
    elif "Three" in line:
        line = line.replace("Three", "Три")
    elif "Four" in line:
        line = line.replace("Four", "Четыре")
    print(line)
    f_new.write(line)
f_new.close()
