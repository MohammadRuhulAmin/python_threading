
#step1- import thread class
from threading import Thread
#create a function containing code to be executed parallay
def display(n,message):
    for i in range(n):
        print(message , n)
#create new thread here
t1 = Thread(target=display,args=(4,"Hi Ruhul Amin"))

# start the new thread
t1.start()