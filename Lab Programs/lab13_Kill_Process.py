import psutil

for proc in psutil.process_iter(['pid','name']):
    print(proc.info)


p_id = int(input("Enter process ID to kill process: "))
           
process = psutil.Process(p_id)
try:
    process.terminate()
except psutil.AccessDenied:
    print(f"Acces Denied to kill: {p_id} ")

