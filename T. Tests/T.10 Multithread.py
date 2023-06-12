"""
1 Threads run in 1 single core
"""
import threading
import time
import random

class MyClass:
    def __init__(self, name):
        self.name = name
        self.x = 0

    def start(self, thread):
        # while True:
        self.x += 1
        time.sleep(random.random()/10)
        self.x -= 1
        print(thread, self.x)


obj = MyClass("my_obj")
if __name__ == "__main__":
    for i in range(2):
        t = threading.Thread(target=obj.start, args=(str(i),)).start()
