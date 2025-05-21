def f(nums):
    c = []
    i = 0
    while i < len(nums):
        j = i
        s = 0
        while j < len(nums) and nums[i] == nums[j]:
            s += nums[j]
            j += 1
        c.append(s)
        i = j
    return c

nums = [2, 2, 3, 3, 3, 4, 4, 1]
r = f(nums)
print(nums)
print(r)