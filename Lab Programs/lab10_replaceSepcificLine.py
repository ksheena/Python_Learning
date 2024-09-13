def ReplaceLine(line_no, line_data):
    fo = open('c:\\Users\\k3bywp8\\text4.txt', 'r')
    data = fo.readlines() 
    if line_no < len(data):
        f1 = open('c:\\Users\\k3bywp8\\text4.txt', 'w')
        f1.writelines(line_data)
    else:
        print(f"Out of index. Please enter the line number with in index {len(data)} starting from 0")


line_no = int(input("Enter the Line Number need to be replaced: "))
New_line_text = input("Enter Text To replace: ")

ReplaceLine(line_no, New_line_text)