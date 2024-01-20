import lock
import threading
import logging
# 互斥锁
# 知乎教程：https://zhuanlan.zhihu.com/p/267650598
lock1 = threading.Lock()
NUM = 0
def thread_1(n):
    # lock1.acquire()
    global NUM
    for i in range(n):
        
        NUM += 1
    # print(f"thread_1 {NUM}")
    # lock1.release()


if __name__ == '__main__': 
    # for i in range(100000):
    t1 = threading.Thread(target=thread_1, args=(1000000,))
    t2 = threading.Thread(target=thread_1, args=(1000000,))
    t1.start()  
    t2.start()
    t1.join()
    t2.join()
    print(NUM)
    print("all threads end")            