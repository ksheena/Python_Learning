# https://www.geeksforgeeks.org/insertion-sort-algorithm/?ref=header_ind

list = [22, 12, 9, 50, 78]

i = 1                                                # value 22
j =0 

n = len(list)
while i <= n-1:                                   #i= 1 , 2
    j = i-1                                       #j =0 , 1
    key = list[i]                                  
    while j >= 0 and key < list[j]:                #0>0       12 < 22 , 1>0 9<22 
        list[j + 1] = list[j]                      #list[1] = 22      
        j -= 1                                     # j = -1 , 0
    list[j + 1] = key                              #list[0] = 12
    print(list)
    i +=1                                          # i= 2                      

print (list)
