import psutil

cpu_time = str(psutil.cpu_times())
print('CPU Time:' + cpu_time)
print(psutil.cpu_times)