import sys
import math

def get_coef(index, prompt):
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

def get_roots(a, b, c):
    D = b**2 - 4*a*c
    roots =[]

    if D > 0:
        root1 = math.sqrt((-b + math.sqrt(D)) / (2*a))
        root2 = math.sqrt((-b - math.sqrt(D)) / (2*a))
        root3 = -root1
        root4 = -root2
        roots.append(root1)
        roots.append(root2)
        roots.append(root3)
        roots.append(root4)

    elif D == 0:
        root1 = math.sqrt(-b / (2*a))
        root2 = -root1
        roots.append(root1)
        roots.append(root2)

    return roots

def print_roots(roots):
    roots_len = len(roots)

    if roots_len == 4:
        print(f"Found 4 roots: {roots[0]}, {roots[1]}, {roots[2]} and {roots[3]}")
    elif roots_len == 2:
        print(f"Found 2 roots: {roots[0]} and {roots[1]}")
    else:
        print("No roots were found")

def main():
    a = get_coef(1, 'Enter A: ')
    b = get_coef(2, 'Enter B: ')
    c = get_coef(3, 'Enter C: ')

    roots = get_roots(a, b, c)
    print_roots(roots)

if __name__ == "__main__":
    main()
