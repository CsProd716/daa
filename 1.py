import random
import time
n=int(input("enter the number of elements"))
aList = [random.randint(0,100) for i in range(n)]
print(aList)
start=time.clock()
for i in range(0, n-1):
  least = i
  for k in range( i + 1 , n ):
    if aList[k] < aList[least]:
      least = k
   aList[least],aList[i]=aList[i],aList[least]
stop=time.clock()
print(aList)
print(stop-start)
