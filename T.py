n = int(input())
a = (n // 1000) % 10
b = (n // 100) % 10
c = (n // 10)%10
d = n % 10
print((a == d) * (b == c) + (a != d) * (b != c) * 2)