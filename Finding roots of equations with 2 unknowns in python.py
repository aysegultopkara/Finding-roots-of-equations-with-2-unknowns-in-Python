print("(a * x**2) + (b * x) + c")
a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))
c = int(input("Enter value for c : "))

d = (b**2) - ( 4 * a * c)
if d > 0:
    print("Roots are Real and Distinct.")
    x1 = (- b - (d ** 0.5)) / (2 * a)
    x2 = (- b + (d ** 0.5)) / (2 * a)
    print(f"{x1} ve {x2}")
elif d == 0:
    print("Roots are Real and Equal.")
    x1 = x2 = - b / (2 * a)
    print(f" {x1} = {x2} ")
else:
    print("Roots are Imaginary.")