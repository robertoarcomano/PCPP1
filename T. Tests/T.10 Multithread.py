"""
1 Threads run in 1 single core
"""
import threading


def fn(name):
    x = 1.1
    while True:
        x = x*2

if __name__ == "__main__":
    for i in range(1,10):
        t = threading.Thread(target=fn, args=(i,))
        t.start()
