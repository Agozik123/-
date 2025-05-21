lesson = int(input())

minut = lesson * 45 + (lesson // 2) * 15 + ((lesson - 1) // 2) * 5
hour = 9 + minut // 60
minut = minut % 60

print(hour, minut)