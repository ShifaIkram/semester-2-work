# Task#2
# Calculate inverse of 2 x 2 matrix(user input) and handle the possible errors occurs.

def matrix_inverse():
    try:
        print("Enter the elements for a 2x2 matrix:")
        # Taking inputs for matrix entries (a,b,c,d)
        a = float(input("Element [0][0] (a): "))
        b = float(input("Element [0][1] (b): "))
        c = float(input("Element [1][0] (c): "))
        d = float(input("Element [1][1] (d): "))

        # Displaying the matrix immediately after input
        print("\nYou entered the following 2x2 matrix:")
        print("-" * 15)
        print(f"| {a:g}   {b:g} |")        # :g(g-tag) = General Format (formatting tool)
        print(f"| {c:g}   {d:g} |")        # By default, it rounds to 6 significant figures &
        print("-" * 15)                    # decides the best way to display a number

        # Calculating the det (ad - bc)
        det = (a * d) - (b * c)
        print(f"\nDeterminant: {det}")

        # Checking if the matrix is singular(to proceed further)
        if det == 0:
            raise ValueError("The matrix is singular (det is 0) and cannot be inverted.")

        # Applying the formula for Inverse: (1/det) * [[d, -b], [-c, a]]
        inv_a = d / det
        inv_b = -b / det
        inv_c = -c / det
        inv_d = a / det

        print("\nThe Inverse Matrix is:")
        print(f"|  {inv_a:g},  {inv_b:g} | \n|  {inv_c:g},  {inv_d:g} |")

    except ValueError as e:
        print(f"Error: {e}")

matrix_inverse()

