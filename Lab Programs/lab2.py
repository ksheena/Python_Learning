
#!/usr/bin/python38

def Check_Palindrome(str):
    if str == str[::-1]:
        print(f"String '{str}' is Palindrome ")               #check whether the string is Symmetrical or Palindrome	
    else:
        print(f"String '{str}' is Not palindrome")


my_str = input("Enter string: ")

print(my_str)

print(f"String After Reverse: {my_str[::-1]}")       # Reverse words in a given String

print(f"Length Of String {len(my_str)}")        # Length of String

char = input("Enter The character that you want to remove from string: ")  #  Ways to remove i'th Character From String Python
cnt = int(input("Enter Number of occurance: "))
str = my_str.replace(char,"", cnt)
print(f"String After removing the value in 2nd index value {str}")       


print(f"Even Number of Index in string : {len(my_str[0:-1:2])}")                   # length of even


Check_Palindrome(my_str)                            # Palindrome Function call



