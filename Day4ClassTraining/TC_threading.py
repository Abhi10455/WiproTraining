import threading
def task():
    print("thread is running")
t1=threading.Thread(target=task)
t1.start()
t1.join()


print("main thread endss")