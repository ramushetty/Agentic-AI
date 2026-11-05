# CPU --> cores can be physical and logical (hyperthreading) 
# single core can run 1 to 2 tasks at the same time (multithreading) but it is not true parallelism.

# if you have 12 cores and you can run 24 tasks at the same time (parallelism) but it is not true parallelism.

# GHZ gigahertz (speed of the CPU) --> 1GHZ = 1 billion cycles per second. (1 cycle = 1 instruction)

# in case of multiple tasks task1,task2,task3,task4 they switch in between each other (context switching) in split seconds (milliseconds) and it is not true parallelism.

# why not parallelism in python? because of GIL (global interpreter lock) which allows only one thread to run at a time. (even if you have multiple cores, only one thread can run at a time)

# if one thread is switching between multiple tasks is called multithreading and if multiple threads are running at the same time is called multiprocessing.

# concurrency is the ability of a program to run multiple tasks at the same time (multithreading) and parallelism is the ability of a program to run multiple tasks at the same time (multiprocessing).

# threads share memory space and processes have their own memory space. (threads are lightweight and processes are heavyweight)

# true parallelism is achieved using multiprocessing and not multithreading.

# python as a software can only run on one thread only - locked by GIL

# threading --> multiple threads --> t1,t2,t3 --> uses os time slicing to switch between threads --> context switching

# process --> multiprocess --> task --> more complex in nature --> CPU intensive task --> 

# asynio (library) --> uses different scheduling algorithm to switch between tasks (not os time slicing) 
# asyncio runs with 1 thread , we can still give multiple tasks 
# giving multiple tasks those are managed by event loop 

# threading lib uses time slicing to switch between threads and it is not true parallelism.
# this switching is nothing but concurrency