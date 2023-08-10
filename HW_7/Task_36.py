# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation_, num_rows_, num_columns_):
    for i in range(1, num_rows_+1):
        res = []
        for j in range(1, num_columns_+1):
            res.append(operation_(i,j))
        print(*res)

num_rows=6
num_columns=6
operation = lambda x,y: x*y

print_operation_table(operation, num_rows, num_columns)