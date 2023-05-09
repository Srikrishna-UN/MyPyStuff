rows = int(input("Enter number of equation / number of rows:"))
columns = int(input("Enter number of variable / number of columns:"))


#
#
# for i in range(columns):
#     eqn_string = input(f"Enter the equation {i+1}:")
#     equations.append(eqn_string.split(" "))


class Matrix:
    def __init__(self, class_rows, class_columns):
        self.equations = []
        self.class_rows = class_rows
        self.class_columns = class_columns

    def input_equations(self, class_rows, class_columns):
        # rows = int(input("Enter number of equation / number of rows:"))
        # columns = int(input("Enter number of variable / number of columns:"))

        for i in range(class_rows):
            eqn_string = input(f"Enter the equation {i + 1}:")
            self.equations.append(eqn_string.split(" "))

        for i in range(class_rows):
            for j in range(class_columns):
                if len(self.equations[i][j]) == self.class_columns:
                    continue
                else:
                    print("Extra/Not enough variables entered ")
                    exit(0)

    def store_equations(self, *args):
        for i in args:
            self.equations.append(i)
        return self.equations

    def access_elements(self, i, j):
        return self.equations[i][j]

    def print_equations(self):
        for _ in self.equations:
            print(f"{_}")


a = Matrix(rows,columns)
b = Matrix(rows,columns)

a.input_equations(rows, columns)
