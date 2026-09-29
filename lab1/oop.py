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
            root1 = (-self.b + math.sqrt(D)) / (2*self.a)
            root2 = (-self.b - math.sqrt(D)) / (2*self.a)
            self.roots.append(root1)
            self.roots.append(root2)
        elif D == 0:
            root = -self.b / (2*self.a)
            self.roots.append(root)

    def print_roots(self):
        roots_len = len(self.roots)
        if roots_len == 2:
            print(f"Found 2 roots: {self.roots[0]} and {self.roots[1]}")
        elif roots_len == 1:
            print("Found 1 root:", *self.roots)
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
