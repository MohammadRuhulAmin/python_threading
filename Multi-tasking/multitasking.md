__What is Multi-tasking in python ?__  
Ans: Executing multiple tasks at the same time.There are two types of multi-tasking  
1. process based multi-tasking  
   --Each task is an indepentent program/process.(Each task can be consider as individual softwares)  
   --Used in OS Level  
2. Thread based multi-tasking  
   --Each task is an independent thread(Separate part of program)  
   --Used in programmatic level  
     (Consider VS code as a program. Then linkter is a thread, Syntax highliter is another thread, Error highliter another thread)  
     
     overall, in process based multi-tasking there are multiple softwares working simulteniously and in Thread based multi-tasking  
     differents features are consider as a thread in a program!


Example:  
    A teacher is teaching 100 students. 10 students per batch then 4 hours will be taking in a hall.  
    If he hires 4 teachers and 4 halls the whole task will be completed in 1 hour.  
    here, 4 teacher are 4 thread and hall is consider memory. 

    __What is Thread ?__ : Thread is an operating system object that executes instructions/program.  
    It is a separate flow of execution in program. Thread represents a task and it is also called   
    sub-program. Considering we have a python script and it has 4 functions.  
    def func_a():   
    def func_b():  
    def func_c():  
    def func_d():  
    if we want to run all of them parallay,then we have to create 4 threads.  
    If we dont make thread(this is an operating system object), the main thread will execute that function.    

    __Need Of Multithreading:__  
    Improve performance of the system or application  
    Reduce response time of websites/applications  
    Normal Program-1 flow  
    Program with n threads:-n flows    

    Applications:-    
    video games  
    multi-media graphics  
    Animations  
    web servers  
    Applications
    




