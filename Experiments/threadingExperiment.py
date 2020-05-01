import time, multithreading

def cpu_heavy(x):
    count = 0
    for i in range(10**10):
        count += i

n_jobs = 4

marker = time.time()
for i in range(n_jobs): cpu_heavy(i)
print("Serial spent", time.time() - marker)
multithreading(cpu_heavy, range(n_jobs), 4)
print("Multithreading spent", time.time() - marker)

