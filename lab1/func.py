import sys
import math

def get_coef(index, prompt, use_argv = True):
    if len(sys.argv) > index and use_argv:
        try:
            coef_str = sys.argv[index]
            coef = float(coef_str)
            return coef
        except:
            print('Invalid console arguement. Try to enter again.')

    coef_str = input(prompt)

    try:
        coef = float(coef_str)
    except:
        print('Invalid input. Try again.')
        coef = get_coef(index, prompt, False)

    return coef

def get_roots(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        root1 = math.sqrt((-b + math.sqrt(D)) / (2*a))
        root2 = math.sqrt((-b - math.sqrt(D)) / (2*a))
        root3 = -root1
        root4 = -root2
        return ('4 roots', root1, root2, root3, root4)

    elif D == 0:
        root1 = math.sqrt(-b / (2*a))
        root2 = -root1
        return ('2 root', root1, root2)
    else:
        return ('no roots')

def print_roots(result_tuple):
    match result_tuple:
        case ('4 roots', root1, root2, root3, root4):
            print(f"Found 4 roots: {result_tuple[1]}, {result_tuple[2]}, {result_tuple[3]} and {result_tuple[4]}")
        case ('2 root', root1, root2):
           print(f"Found 2 roots: {result_tuple[1]} and {result_tuple[2]}")
        case ('no roots'):
            print("No roots were found")

def main():
    a = get_coef(1, 'Enter A: ')
    b = get_coef(2, 'Enter B: ')
    c = get_coef(3, 'Enter C: ')

    roots = get_roots(a, b, c)
    print_roots(roots)

if __name__ == "__main__":
    main()
