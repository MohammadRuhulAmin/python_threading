__What is main thread ?__   
Ans: Python interpreter start and then request Operating system to create one thread which is called Main Thread.  
which is also called default. Main thread is created by PVM python virtual machine(Interprater).  
Threads are python objects of threading Thread() class.

make sure the name of the script will be my_threading.py

```python
import threading
print(threading.current_thread())
# every thread has thread id
#<_MainThread(MainThread, started 13736)>
# here MainThread is the name of the thread
# status is started
# i3736 is the id of that thread

print(threading.current_thread().name) # will print the name of that thread only
print(threading.current_thread().ident)# will print the Thread id
print(threading.current_thread().is_alive())# will print if thread running or not !




