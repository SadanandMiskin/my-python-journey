import numpy as np
import time

SIZE=1000000
l1=range(SIZE)
l2=range(SIZE)

a1=np.arange(SIZE)
a2=np.arange(SIZE)

start = time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print(time.time() - start)
# print(result)

start=time.time()
result=a1+a2
print(time.time() - start)
# print(result)