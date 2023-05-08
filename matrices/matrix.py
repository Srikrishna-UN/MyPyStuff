

# rows = int(input("Enter number of equation / number of rows:"))
# columns = int(input("Enter number of variable / number of columns:"))
#
# equations = []
#
# for i in range(columns):
#     eqn_string = input(f"Enter the equation {i+1}:")
#     equations.append(eqn_string.split(" "))


class Matrix:
    def __init__(self):
        self.equations = []

    def input_equations(self):
        rows = int(input("Enter number of equation / number of rows:"))
        columns = int(input("Enter number of variable / number of columns:"))

        for i in range(rows):
            eqn_string = input(f"Enter the equation {i + 1}:")
            self.equations.append(eqn_string.split(" "))

    def store_equations(self, *args):
        for i in args:
            self.equations.append(i)
        return self.equations

    def access_elements(self, i, j):
        return self.equations[i][j]

    def print_equations(self):
        for _ in self.equations:
            print(f"{_}")


a = Matrix()
# a.input_equations()
# a.print_equations()
print(a.store_equations([1, 2, 3], [3, 4, 5]))



