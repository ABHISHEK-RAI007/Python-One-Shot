n = int(input('Enter size of list:'))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input('Enter index1:'))
idx2 = int(input('Enter index2:'))
print(list)

#  swapping values a idx1 and idx2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)
