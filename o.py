def total(a,b,n):
    price_kopecks = a*100+b 
    total_kopecks = price_kopecks*n
    rubles = total_kopecks//100
    kopecks = total_kopecks%100
    return rubles,kopecks
a = int(input())
b = int(input())
n = int(input())
rubles,kopecks = total(a,b,n)
print(rubles, kopecks)

















































































1
def function(Python):
  result = ''.join(chr(ord(i1) - 32 if 'a' <= i1 <= 'z' else ord(i1) + 32 if 'A' <= i1 <= 'Z' else ord(i1)) for i1 in reversed(Python))
  return result

input1 = input("Input words: ")
answer = function(input1)
print(answer)

#2

def sssascii(name):

     maxsequences = ""
     oursentences = name[0]

     for i in range(1,len(name)):
         if ord(name[i]) == ord(name[i-1]) + 1:
             oursentences +=name[i]
         else:
             if len(oursentences)>len(maxsequences):
                 maxsequences = oursentences
             oursentences =name[i]

     if len(oursentences)>len(maxsequences):
         maxsequences = oursentences

     return maxsequences
print(sssascii(input("")))

#3
def countletter(l):
    mass = {}
    for x in l:
        if x in mass:
            mass[x]+=1
        else:
            mass[x] = 1

    mass_list = list(mass.items())

    #сортировка по алфв
    for i in range(len(mass_list)-1):
        for j in range(i+1, len(mass_list)):
            if mass_list[i][0] > mass_list[j][0]:  #при/но так работает: берет b и a: b>a(это правильно потому что:a<b<c<d<e, оно так работает)
                mass_list[i],mass_list[j] = mass_list[j], mass_list[i]

   #сортировка по убыванию количеств
    for i in range(len(mass_list)-1):
       for j in range(i+1, len(mass_list)):
           if mass_list[i][1]<mass_list[j][1]:
               mass_list[i],mass_list[j] = mass_list[j], mass_list[i]
    return mass_list
print(countletter(input("")))



#4
def letttt(numberss ,k):
    k = k%len(numberss)
    return numberss[-k:] + numberss[:-k]
numberss = list(map(int, input("списко намберов: ").split()))
k = int(input("k: "))
print(letttt(numberss,k))

#5
def twolists(list1,list2):
    connection = []
    len1, len2 = len(list1),len(list2)
    min_len =  min(len1,len2)

    for i in range(min_len):
        connection.append(list1[i])
        connection.append(list2[i])
    connection.extend(list1[min_len:])
    connection.extend(list2[min_len:])
    return connection
list1 = ['a', 'b', 'c', 'd']
list2 = [1,2,3]
print(twolists(list1,list2))

#6
def palindr(s):
    longest = ''

    for i in range(len(s)):  # Начальная позиция подстроки
        for j in range(i, len(s)):  # Конечная позиция подстроки
            strr = s[i:j+1]  # Берем подстроку
            rev = ''
            for x in strr:
                rev = x + rev
            if strr == rev and len(strr) > len(longest):
                longest = strr

    return longest

s = input("")
print("Самая длинная палиндромная подстрока:", palindr(s))

#7
def summlistt(nums):
    result = []  # Итоговый список
    current_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_sum += nums[i]
        else:
            result.append(current_sum)
            current_sum = nums[i]

    result.append(current_sum)

    return result
nums = list(map(int, input("числа через пробел: ").split()))
print(summlistt(nums))

#8
def luntik(matrix):
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

n, m = map(int, input("Размер матрицы: ").split())
matrix = [list(map(int, input().split())) for _ in range(n)]
luntik(matrix)

#9
def secondfrequent(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    freq_list = list(freq.items())

    for i in range(len(freq_list) - 1):
        for j in range(i + 1, len(freq_list)):
            if freq_list[i][1] < freq_list[j][1]:
                freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

    if len(freq_list) < 2:
        return None

    return freq_list[1][0]

words = input("введи слова через пробел: ").split()
print(secondfrequent(words))


#10
def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
nums = [3, 4, -1, 1]
print(first_missing_positive(nums))