import random
import time
count = 0
def merge_sort(li):
  if len(li) < 2: return li
    m = len(li) // 2
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))
def merge(l, r):
  global count
  result = []
  i = j = 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      result.append(l[i])
      i += 1
    else:
      result.append(r[j])
      count = count + (len(l) - i)
      j += 1
  result.extend(l[i:])
  result.extend(r[j:])
  return result
n = int(input("Enter number of elements in the list"))
unsorted = [random.randint(0,100) for i in range(0,n)]
print("Unsorted list" , unsorted)
start = time.clock()
print ("Sorted List" , merge_sort(unsorted))
stop = time.clock()
print ("Number of inversions = " ,count , "\nTime taken", stop-start )
