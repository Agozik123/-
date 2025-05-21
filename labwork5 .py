def calculate_gpa():
    total_weighted_marks = 0
    total_credits = 0
    num_courses = int(input("Enter the number of courses: "))

    for i in range(num_courses):
        marks = float(input("Enter the marks (0-100): "))
        credits = float(input("Enter the credits: "))

        if marks >= 90: gpa_score = 4.0
        elif marks >= 80: gpa_score = 3.0
        elif marks >= 70: gpa_score = 2.0
        elif marks >= 60: gpa_score = 1.0
        else: gpa_score = 0.0

        total_weighted_marks += gpa_score * credits
        total_credits += credits

    if total_credits > 0:
        gpa = total_weighted_marks / total_credits
        print(f"Your overall GPA is: {gpa:.2f}")
    else:
        print("Error: Total credits cannot be zero.")

calculate_gpa()
