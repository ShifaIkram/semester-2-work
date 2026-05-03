# Task#5
# Function to calculate GPA
# GPA = total grade points/ total credit hours

def calculate_gpa():
    subjects = int(input("Enter number of subjects: "))

    total_grade_points = 0
    total_credit_hours = 0

    for i in range(1, subjects + 1):
        print("\nSubject", i)
        grade_point = float(input("Enter Grade Points: "))
        credit_hours = float(input("Enter Credit Hours: "))

        total_grade_points += grade_point * credit_hours
        total_credit_hours += credit_hours

    gpa = total_grade_points / total_credit_hours
    return gpa

# Call the function
result = calculate_gpa()

print("\nYour Semester GPA is:", round(result, 2))