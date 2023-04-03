import multiprocessing
import time

t1=time.time()

def worker(num):
    return print(num*2)

if __name__=='__main__':
    jobs = []
    for i in range(100):
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()

    print(t1-time.time())

import threading
import time

time1=time.time()
def count(num: int):
    return print(num*2)

for n in range(100):
    thread = threading.Thread(target=count,args=(n,))
    thread.start()
    #count(n)

print(time.time()-time1)