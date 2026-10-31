import sys
import math

class SquareEquation:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []

    def get_coef(self, index, prompt):
        if (index < len(sys.argv)):
            try:
                coef = float(sys.argv[index])
                return coef
            except:
                print('Invalid console arguement. Try to enter again.')
        while True:
            coef = input(prompt)
            try:
                coef = float(coef)
                return coef
            except:
                print('Invalid input. Try again.')


    def get_roots(self):
        D = self.b**2 - 4*self.a*self.c
        if D > 0:
            root1 = math.sqrt((-self.b + math.sqrt(D)) / (2*self.a))
            root2 = math.sqrt((-self.b - math.sqrt(D)) / (2*self.a))
            root3 = -root1
            root4 = -root2
            self.roots.append(root1)
            self.roots.append(root2)
            self.roots.append(root3)
            self.roots.append(root4)
        elif D == 0:
            root1 = math.sqrt(-self.b / (2*self.a))
            root2 = -root1
            self.roots.append(root1)
            self.roots.append(root2)

    def print_roots(self):
        roots_len = len(self.roots)
        if roots_len == 4:
            print(f"Found 4 roots: {self.roots[0]}, {self.roots[1]}, {self.roots[2]} and {self.roots[3]}")
        elif roots_len == 2:
            print(f"Found 2 roots: {self.roots[0]} and {self.roots[1]}")
        else:
            print("No roots were found")

def main():
    equation = SquareEquation()

    equation.a = equation.get_coef(1, 'Enter A: ')
    equation.b = equation.get_coef(2, 'Enter B: ')
    equation.c = equation.get_coef(3, 'Enter C: ')

    equation.get_roots()
    equation.print_roots()

if __name__ == "__main__":
    main()
