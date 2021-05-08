"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
f = open("DZ5_2.txt")
lines = f.readlines()
print(f"DZ5_2.txt содержит  {len(lines)} строк")
for step, line in enumerate(lines, start=1):
    print(f"и {len(line.split())} слов в строке {step}")
f.close()
