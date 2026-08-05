##process that run in parallel 
## parallel execution multiple cores of the cpu

import multiprocessing

import time

def sequare_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__=="__main__":
##create 2 process

    p1=multiprocessing.Process(target=sequare_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()


##a=start the process
    p1.start()
    p2.start()

##wait for the process to complete
    p1.join()
    p2.join()


    finished_time=time.time()-t
    print(finished_time)