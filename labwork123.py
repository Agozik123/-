k = float(input("weight (kg): "))
m = float(input("height (m): "))
if k > 0 and m > 0:
    b = k / m**2
    if b < 18.5:
        print("Underweight")
    elif b < 25:
        print("Normal")
    else:
        print("Overweight")
else:
    print("Invalid input")
