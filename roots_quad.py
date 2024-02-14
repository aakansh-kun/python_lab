import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
    else:
        root1 = root2 = -b / (2*a)
        imaginary = math.sqrt(-discriminant) / (2*a)
        root1 = complex(root1, imaginary)
        root2 = complex(root2, -imaginary)

    return root1, root2

a = int(input("enter coefficient of x^2: "))
b = int(input("enter coefficient of x: "))
c = int(input("enter constant: "))

root1, root2 = find_roots(a, b, c)
print("The roots are root1 and root2", root1,root2)
