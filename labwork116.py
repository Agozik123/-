def f(aboba, bobsb):
    asbd = len(aboba)
    if asbd == 0:
        return aboba
    bobsb = bobsb % asbd
    cdsc = aboba[-bobsb:] + aboba[:-bobsb]
    return cdsc
s = [1, 2, 3, 4, 5]
k = 2
o = f(s, k)
print(o)