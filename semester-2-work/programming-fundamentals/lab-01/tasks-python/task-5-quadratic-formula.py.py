# Task#5
# Quadratic Formula and Nature of Roots

# Taking input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Discriminant
print("-------- NATURE OF ROOTS ---------")
print("DISCRIMINANT: b^2 - 4ac")
disc = b*b - 4*a*c

# Nature of roots
if disc > 0:
    print("Roots are real, distinct and irrational.")
elif disc == 0:
    print("Roots are real, equal and rational.")
else:
    print("Roots are imaginary.")

# Finding value of roots only if real
print("-------- ROOTS OF QUADRATIC EQUATION ---------")
print("QUADRATIC FORMULA: -b + (b^2 -4ac)/ 2a , -b - (b^2 -4ac)/ 2a")
if disc >= 0:
    root1 = (-b + disc**0.5) / (2*a)
    root2 = (-b - disc**0.5) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
