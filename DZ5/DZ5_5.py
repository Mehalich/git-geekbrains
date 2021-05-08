"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
f = open("DZ5_5.txt", "w+")
f.write("1 2 3 4 5 6 7 8 9 0")
f.seek(0)
line = f.readlines()
result = 0
line = str(line[0])
line = line.split()
for step in line:
    result += int(step)
print(result)
f.close()
