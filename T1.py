n = input()
n = "0 "* (4 - len(n)) + n 
a = n[0]
b = n[1]
c = n[2]
d = n[3]
print((a == b ) * (b == c) + 1)