# Python 2
# import thread  # depricated

# Python 3
import threading

# Using Python 2 threading in Python 3
# import _thread

import time

# create a function that acts a thread
def func():
	print("ran")
	time.sleep(1)
	print("done")

# create a function that acts a thread
def func2(x:str):
	print("ran :",str)
	time.sleep(1)
	print("done :",str)

x = threading.Thread(target=func, args=())
# A new thread, apart from the main thread, starts
x.start()
print(threading.activeCount())  # 2

# For tuple, add extra comma, last one gets removed
# (5,) => (5,None)
y = threading.Thread(target=func2, args=('ayush',))
y.start()
print(threading.activeCount())  # 3

# ================= E X A M P L E : 2 ================================

def count(n):
	for i in range(1, n+1):
		print(i)
		time.sleep(0.01)

for _ in range(2):
	x = threading.Thread(target=count, args = (10,))
	x.start()

print("Done")
