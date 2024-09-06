
#!/usr/bin/python38

def swp_first_last(list):
    temp_var = list1[0]
    list1[0] = list1[-1]          #interchange first and last elements in a list
    list1[-1] = temp_var  
    return list1               

def swap_element(list, index1, index2):
    val = list1[index1], list1[index2]
    list1[index2], list1[index1] = val      # swap two elements in a list		
    return list1

def maxof2(num1, num2):                # Maximum of two numbers in Python
    if num1>num2:
        max = num1
    else:
        max = num2
    return max

def minof2(num1, num2):            #  Minimum of two numbers in Python
    if num1<num2:
        min = num1
    else:
        min = num2
    return min

list1 = [10, 22, 33, 44, 55, 66]

print(f"Entered List is: {list1}")

print(f"length of string {len(list1)}")                 #  Length of list

print(f"List after swapping first and last element {swp_first_last(list1)}")       # swp_first_last(list1) function call and print           

print(f"Get position of two elements to swap")
index1 = int(input("Enter First Position:"))
index2 = int(input("Enter Second Second:"))

print(f"List after swapping  elements {swap_element(list1, index1-1, index2-1)}")    # Swap any two element based on its postion. swap_element(list1, index1-1, index2-1) -> function call and print



print(f"MAX value in the list is: {max(list1)}")         # max and min value in list
print(f"MIN value in the list is: {min(list1)}")


print(f"\n Calulating max and min of two numbers")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

max = maxof2(num1, num2)                 
print(f"Max of two numbers : {max}")    

min = minof2(num1, num2)
print(f"Min of two numbers : {min}")
