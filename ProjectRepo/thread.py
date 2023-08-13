
#step1- import thread class
from threading import Thread,current_thread
#create a function containing code to be executed parallay

def display_1(n):
    print("T1 Thread details:",current_thread())
    print("T1 Thread details:", current_thread().name)
    print("T1 Thread details:", current_thread().ident)
    for i in range(n):
        print("Hii")

def display(n,message):
    for i in range(n):
        print(message, n)
#create new thread here
t1 = Thread(target=display,args=(4,"Hi Ruhul Amin"))
t2 = Thread(target=display_1,args=(5,))
# start the new thread
t2.start()
t1.start()
