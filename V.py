a = int(input())
b = int(input())
d = a - b
k = (d // (abs(d) + 1)) + 1 
print(a * k + b * (1 - k)) 