#!/usr/bin/python38


def commonval_inList(my_list1, my_list2):                #Check two lists have atleast one element common Method1
    i = 0
    j = 0
    len1 = len(my_list1)
    len2 = len(my_list2)

    list3 = []
    print(f"Common Element in List:")
    while i <= len1-1:
        while j <= len2-1:
            if my_list1[i] == my_list2[j]:
                list3.append(my_list1[i])
            j +=1
        i +=1
        j = 0
    return list3

def commonval_inList_usingset(my_list1, my_list2):               # Check two lists have atleast one element common Method 2 
    my_set1 = set(my_list1)
    my_set2 = set(my_list2)
    if my_set1 & my_set2:
        print(my_set1 & my_set2)

def main():
    my_set = {11, 12, 23, 24, 26}

    print(f"Size of set is: {len(my_set)}")                             # size of a Set 

    print(my_set)
    index = 0                                                           # Iterate over a set in Pytho
    for val in my_set:
        print(f"Value at index [{index}] = {val}")
        index +=1


    print(f"Minimun value of set is {min(my_set)} ")                  # Max and Min value in Set     
    print(f"Maximum value of set is {max(my_set)} ")


    my_list1 = [10, 20, 30, 40, 50]
    my_list2 = [50, 60, 70, 80, 10]

    print(f"List 1: {my_list1}  List2: {my_list2}")
    commn_values = commonval_inList(my_list1, my_list2)                # Check common value method1 function call 
    print(f"Common values in Lists {commn_values}")

    commonval_inList_usingset(my_list1, my_list2)                       # Check common value method2 function call 


if __name__ == "__main__":
    main()
