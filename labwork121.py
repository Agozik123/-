def f(w):
  if not w:
    return None
  s = {}
  for word in w:
    s[word] = s.get(word, 0) + 1
  ss = sorted(s.items(), key=lambda x: x[1], reverse=True)
  return ss[1][0] if len(ss) > 1 else None
w = ["apple", "banana", "apple", "orange", "banana", "banana", "grape"]
r = f(w)
print(w)
print(r)