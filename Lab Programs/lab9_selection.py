# Selection Sort https://www.geeksforgeeks.org/selection-sort-algorithm-2/

list = [10, 22, 9, 50, 78]

i = 0
j =0 

n = len(list)
while i <= n-1:
    j = i+1
    while j <= n-1:
        if list[i] > list[j]:
            temp = list[i], list[j]
            list[j], list[i] = temp
        j += 1
    i +=1

print(list)
