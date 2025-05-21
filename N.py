def lesson_end_time(n):
    total_time = 45 * n + 5 * ((n - 1) // 2) + 15 * ((n - 1) // 2)
    hours = 9 + total_time // 60
    minutes = total_time % 60
    return hours, minutes

n = int(input())
hours, minutes = lesson_end_time(n)
print(hours, minutes)
