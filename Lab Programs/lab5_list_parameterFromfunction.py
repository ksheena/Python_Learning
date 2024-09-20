import inspect 

def add_num(a: int, b: int):
    return a+b

print(add_num(3,4))

print(f"Paramerts in the defined function : {inspect.signature(add_num)}")

print(f"parameters in in-built function 'len' : {inspect.signature(len)} ")