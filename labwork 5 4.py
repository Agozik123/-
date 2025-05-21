def student_gpa():
    students = []
    while True:
       name = input("Enter name(or 'done' to finish): ")
        if name.lower() == 'done':
            break
        gpa = float(input("Enter GPA: "))
        students.append((name, gpa))

    with open("wwww.txt", "w") as file:
        for name, gpa in students:
            file.write(f"{name}: {gpa}\n")

    print("Students data saved to students.txt.")
    avg_gpa = sum(gpa for _, gpa in students) / len(students)
    print(f"Average GPA: {avg_gpa:.2f}")


student_gpa()
