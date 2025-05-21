a = int(input())
b = int(input())

c = (a - b)
d = (c // (abs(c) if c != 0 else 1)) * c // (c if c != 0 else 1)
e = (a * (d == 0)) + (b * (d != 0))

print(e)