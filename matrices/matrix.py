rows = int(input("Enter number of equation / number of rows:"))
columns = int(input("Enter number of variable / number of columns:"))
matrices = ['a', 'b', 'c', 'd']


class Matrix:
    def __init__(self, class_rows, class_columns):
        self.equations = []
        self.class_rows = class_rows
        self.class_columns = class_columns

    def input_equations(self):

        for i in range(self.class_rows):
            eqn_string = input(f"Enter the equation {i + 1}:")
            self.equations.append(eqn_string.split(" "))

        for x in range(self.class_rows):
            if len(self.equations) != self.class_rows and len(self.equations[x]) != self.class_columns:
                print("Error brooo! Check variables entered")

    def store_equations(self, *args):
        for i in args:
            self.equations.append(i)
        return self.equations

    def access_element(self, i, j):
        return self.equations[i][j]

    def print_equations(self):
        for _ in self.equations:
            print(f"{_}")

    def get_matrix(self):
        return self.equations

    def get_rank(self):
        return [self.class_rows, self.class_columns]

    def scalar_multiplication(self, k):
        for m in range(self.class_rows):
            for n in range(self.class_columns):
                self.equations[m][n] = int(self.equations[m][n])
                self.equations[m][n] *= k
                self.equations[m][n] = str(self.equations[m][n])
        return self.equations

    def transpose(self):
        for i in range(self.class_rows):
            for j in range(self.class_columns):
                self.equations[i][j] = self.equations[j][i]
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
a.input_equations()
print(a.transpose())

