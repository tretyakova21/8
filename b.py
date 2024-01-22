def fill_array_diagonal(n):
    array = [[0] * n for _ in range(n)]

    for i in range(n):
        array[i][n - 1 - i] = 1  # Правая верхняя диагональ
        for j in range(n - 1 - i):
            array[i][j] = 0  # Выше правой диагонали
            array[j][i] = 2  # Ниже правой диагонали

    return array

def fill_star_array(n):
    array = [['.' for _ in range(n)] for _ in range(n)]

    middle = n // 2
    for i in range(n):
        array[i][middle] = '*'  # Средний столбец
        array[middle][i] = '*'  # Средняя строка
        array[i][i] = '*'  # Главная диагональ
        array[i][n - 1 - i] = '*'  # Побочная диагональ

    return array

def fill_diagonal_numbers(n):
    array = [[abs(i - j) for j in range(n)] for i in range(n)]

    return array

# Задача 1
n_diagonal = int(input("Введите размерность массива для задачи 1: "))
array_diagonal = fill_array_diagonal(n_diagonal)
print("\nЗадача 1:")
for row in array_diagonal:
    print(*row)

# Задача 2
n_star = int(input("\nВведите нечетное число для задачи 2: "))
array_star = fill_star_array(n_star)
print("\nЗадача 2:")
for row in array_star:
    print(*row)

# Задача 3
n_numbers = int(input("\nВведите размерность массива для задачи 3: "))
array_numbers = fill_diagonal_numbers(n_numbers)
print("\nЗадача 3:")
for row in array_numbers:
    print(*row)
