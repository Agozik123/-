def f(s):
  a = ""
  b = ""
  for i in range(len(s)):
    if i > 0 and ord(s[i]) == ord(s[i-1]) + 1:
      b += s[i]
    else:
      b = s[i]
    if len(b) > len(a):
      a = b
  return a

s = "abcfghijklmnxyz12345"
o = f(s)
print(o)

s = "abcdeghijklmnopqrstuvwxyz"
o = f(s)
print(o)

s = "1234567890"
o = f(s)
print(o)

s = ""
o = f(s)
print(o)

s = "a"
o = f(s)
print(o)

s = "ab"
o = f(s)
print(o)