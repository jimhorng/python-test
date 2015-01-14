'''
Created on Oct 21, 2014

@author: jimhorng
'''
from threading import Thread
import time

def main():
    t = Thread(target=thread_task1)
    t.start()
    time.sleep(50)

def thread_task1():
    time.sleep(100)
    
if __name__ == '__main__':
    main()