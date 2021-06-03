"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_data):
        self.data = matrix_data

    def __str__(self):
        mat_result = ""
        for line in self.data:
            for step in line:
                mat_result = mat_result + str(step) + " "
            mat_result = mat_result + "\n"
        return mat_result

    def __add__(self, other):
        result = ""
        for line_1, line_2 in zip(self.data, other.data):
            for step_1, step_2 in zip(line_1, line_2):
                result_line = step_1 + step_2
                result = result + str(result_line) + " "
            result = result + "\n"
        return result


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
