# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:48:09 2019

@author: MartinTropse
"""

import concurrent.futures
import time
import multiprocessing
from multiprocessing import Pool

#There are a few issues with running multiprocessing with spyder, by running it externally helps
#Run > Configuration per file > Execute in an external system terminal



# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'

# #some issue here :o Probably because of Spyder
# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5, 4, 3, 2, 1]
#         results = executor.map(do_something, secs)
#         print("This occurs?")
    
#         # for result in results:
#         #     print(result)
#     finish = time.perf_counter()
#     print(f'Finished in {round(finish-start, 2)} second(s)')
  
# results = list(map(do_something, secs))

def aSpawn(num):
    print(f"Spawn{num}")

#, args=(i, )
if __name__ == '__main__':
    for i in range(30):
        p = multiprocessing.Process(target=aSpawn, args=(i,))
        p.start()
        #p.join()
        
#For some reason this cannot be run from the spyder IDE? It works through the powershell

def job(num):
    return num*2

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(job, [1,2,3]))


#Example of threading with concurrent futures module.
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')