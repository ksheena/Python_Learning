import psutil

def Get_process():
    result = []
    for i in psutil.process_iter(['pid','name','username']):  
        result.append(i.info)
    return result

for poc in Get_process():
    print(poc)
    