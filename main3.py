a = int(input())
b = int(input())
n = int(input())

total_cop = (a * 100 + b) * n
ryb = total_cop // 100
cop = total_cop % 100

print(ryb, cop)
