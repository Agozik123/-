def e(list1, list2):
  a = []
  i = 0
  j = 0
  while i < len(list1) and j < len(list2):
    a.append(list1[i])
    a.append(list2[j])
    i += 1
    j += 1
  while i < len(list1):
    a.append(list1[i])
    i += 1
  while j < len(list2):
    a.append(list2[j])
    j += 1
  return a
list1 = [1, 2, 3, 4, 7]
list2 = ['a', 'b', 'c',"d"]
cherez_probel_list = e(list1, list2)
print(list1)
print(list2)
print(cherez_probel_list)