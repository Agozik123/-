def f(s):
    if not s:
        return ""
    l = ""
    for i in range(len(s)):
        a, b = i, i
        while a >= 0 and b < len(s) and s[a] == s[b]:
            if (b - a + 1) > len(l):
                l = s[a:b + 1]
            a -= 1
            b += 1
        a, b = i, i + 1
        while a >= 0 and b < len(s) and s[a] == s[b]:
            if (b - a + 1) > len(l):
                l = s[a:b + 1]
            a -= 1
            b += 1

    return l

s = "racecarbanana"
r = f(s)
print(f"Input: {s}")
print(f"Longest Palindrome: {r}")
