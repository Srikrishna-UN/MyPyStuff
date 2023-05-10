rows = int(input("Enter number of equation / number of rows:"))
columns = int(input("Enter number of variable / number of columns:"))


class Matrix:
    def __init__(self, class_rows, class_columns):
        self.equations = []
        self.class_rows = class_rows
        self.class_columns = class_columns

    def input_equations(self, class_rows, class_columns):

        for i in range(class_rows):
            eqn_string = input(f"Enter the equation {i + 1}:")
            self.equations.append(eqn_string.split(" "))

        for x in range(class_rows):
            if len(self.equations) != self.class_rows and len(self.equations[x])!=self.class_columns:
                print("Error brooo! Check variables entered")

    def store_equations(self, *args):
        for i in args:
            self.equations.append(i)
        return self.equations

    def access_elements(self, i, j):
        return self.equations[i][j]

    def print_equations(self):
        for _ in self.equations:
            print(f"{_}")

    def get_matrix(self):
        return self.equations


def sum_matrices(*args, func_rows, func_columns):
    func_sum_matrix = [[0 for j in range(func_columns)] for i in range(func_rows)]
    for x in args:
        x_matrix = x.get_matrix()
        for m in range(func_rows):
            for n in range(func_columns):
                func_sum_matrix[m][n] += int(x_matrix[m][n])
    return func_sum_matrix


a = Matrix(rows,columns)
b = Matrix(rows,columns)
c = Matrix(rows,columns)
a.input_equations(rows, columns)
b.input_equations(rows, columns)
c.input_equations(rows, columns)

sum_matrix = sum_matrices(a, b, c, func_rows=rows, func_columns=columns)
print(sum_matrix)
