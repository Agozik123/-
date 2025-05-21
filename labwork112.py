def f(𓂺):
  a = ""
  b = ""
  for i in range(len(𓂺)):
    if i > 0 and ord(𓂺[i]) == ord(𓂺[i-1]) + 1:
      b += 𓂺[i]
    else:
      b = 𓂺[i]
    if len(b) > len(a):
      a = b
  return a
𓂺 = "abcfghijklmnxyz12345"
o = f(𓂺)
print(o)
𓂺 = "abcdeghijklmnopqrstuvwxyz"
o = f(𓂺)
print(o)
𓂺 = "1234567890"
o = f(𓂺)
print(o)