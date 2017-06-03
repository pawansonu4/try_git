import threading
import time
a=[]
b=[]
def fun1():
    if threading.current_thread().getName()=="thread1":
        for i in range(5000):
            a.append(i)

    else:
        for i in range(5000,10000):
            a.append(i)


t=threading.Thread(name='thread1', target=fun1)
t1=threading.Thread(name='thread2', target=fun1)
t.start()
t1.start()
t.join()
t1.join()
print(a)
print(b)