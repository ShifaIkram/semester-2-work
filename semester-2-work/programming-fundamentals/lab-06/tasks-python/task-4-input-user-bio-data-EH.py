# Task#4
# Taking user's Bio-Data and raising Exceptions

def collect_bio_data():
    try:
        # Input Collection
        name = input("Enter Name: ")
        # Exception 1 : Checking if the entered name contains any digits
        if any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain digits.")

        address = input("Enter Address: ")
        # Exception 2 : Check length of the address (!<3)
        if len(address) < 3:
            raise ValueError("Address must be at least 3 characters long.")

        contact = input("Enter Contact No.: ")
        # Check if contact no. contains any alphabets
        if any(char.isalpha() for char in contact):
            raise ValueError("Contact number cannot contain alphabets.")

        age = int(input("Enter Age: "))
        # Checking for the age range
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150.")

        gender = input("Enter Gender (male/female): ").strip().lower()
        # Check gender options
        if gender not in ['male', 'female']:
            raise ValueError("Gender must be either 'male' or 'female'.")

        # Displaying the Data if all checks pass
        print("\n --- Bio Data Collected Successfully ---")
        print(f"Name:    {name}")
        print(f"Address: {address}")
        print(f"Contact: {contact}")
        print(f"Age:     {age}")
        print(f"Gender:  {gender.capitalize()}")

    except ValueError as e:
        print(f"\nData Entry Error: {e}")


collect_bio_data()