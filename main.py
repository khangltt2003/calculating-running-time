import time
import random
import csv
#quick sort with first element as pivot
def quickSort(arr):
  if(len(arr) <= 1): return arr
  pi = arr[0]
  lArr = [x for x in arr[1:] if x < pi]
  rArr = [x for x in arr[1:] if x > pi]
  return quickSort(lArr)  + [pi] + quickSort(rArr)

#quick sort with random element as pivot
def randomQuickSort(arr):
  if(len(arr) <= 1): return arr
  pi = arr[random.randint(0, len(arr)-1)]
  lArr = [x for x in arr if x < pi]
  rArr = [x for x in arr if x > pi]
  return quickSort(lArr)  + [pi] + quickSort(rArr)


def merge(arr, left, mid, right):
  lSize = mid - left + 1
  rSize  = right - mid
  lArr = [-1] * lSize
  rArr = [-1] * rSize
  for i in range(0, lSize):
    lArr[i] = arr[left + i]
    
  for i in range(0, rSize):
    rArr[i] = arr[mid + 1 + i]

  i = 0
  j = 0
  k = left
  while(i < lSize and j < rSize):
    if(lArr[i] < rArr[j]):
      arr[k] = lArr[i]
      i+=1
    else:
      arr[k] = rArr[j]
      j+=1
    k+=1
  
  while(i < lSize):
    arr[k] = lArr[i]
    k+=1
    i+=1
    
  while(j < rSize):
    arr[k] = rArr[j]
    k+= 1
    j+=1

def mergeSortHelper(arr, left, right):
  if(left< right):
    mid = left + (right - left)//2
    mergeSortHelper(arr, left, mid)
    mergeSortHelper(arr, mid+1, right)
    merge(arr, left, mid, right)
    
def mergeSort(arr):
  mergeSortHelper(arr, 0, len(arr) - 1)


data1 = [["arr = [n, n−1, ..., 3, 2, 1]"], ["","2^5", "2^6", "2^7","2^8","2^9"]]
temp = ["Quick Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)][::-1]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  begin = time.perf_counter_ns()
  sortedArray = quickSort(arr1)
  end = time.perf_counter_ns() 
  if(arr2 == sortedArray):
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data1.append(temp)

temp = ["Randomized Quick Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)][::-1]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  begin = time.perf_counter_ns()
  sortedArray = randomQuickSort(arr1)
  end = time.perf_counter_ns()
  if(arr2 == sortedArray):
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data1.append(temp)

temp = ["Merge Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)][::-1]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  begin = time.perf_counter_ns()
  mergeSort(arr1)
  end = time.perf_counter_ns()
  if(arr2 == arr1):
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data1.append(temp)

data2 = [["arr is a random permutation of [1, 2, ..., n]"], ["","2^5", "2^6", "2^7","2^8","2^9"]]
temp = ["Quick Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  random.shuffle(arr1)
  begin = time.perf_counter_ns()
  sortedArray = quickSort(arr1)
  end = time.perf_counter_ns()
  if(arr2 == sortedArray):
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data2.append(temp)

temp = ["Randomized Quick Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  random.shuffle(arr1)
  begin = time.perf_counter_ns()
  sortedArray = randomQuickSort(arr1)
  end = time.perf_counter_ns()
  if(arr2 == sortedArray):
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data2.append(temp)

temp = ["Merge Sort"]
for i in range(5, 10):
  arr1 = [x for x in range(1, pow(2,i)+1)]
  arr2 = [x for x in range(1, pow(2,i)+1)]
  random.shuffle(arr1)
  begin = time.perf_counter_ns()
  mergeSort(arr1)
  end = time.perf_counter_ns() 
  if(arr2 == arr1):
    temp.append(round(end-begin))
  else:
    temp.append("failed")

data2.append(temp)

data3 = [["arr = [1, 3, . . . , n − 1, 2, ... , n]"], ["","2^5", "2^6", "2^7","2^8","2^9"]]
temp = ["Quick Sort"]
for i in range(5, 10):
  odd = [x for x in range(1, pow(2,i), 2)]
  even = [x for x in range(2, pow(2,i)+1, 2)]
  arr2 = [x for x in range(1, pow(2,i) + 1)]
  arr = odd + even
  begin = time.perf_counter_ns()
  sortedArray = quickSort(arr)
  end = time.perf_counter_ns()
  if sortedArray == arr2:
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data3.append(temp)

temp = ["Randomized Quick Sort"]
for i in range(5, 10):
  odd = [x for x in range(1, pow(2,i), 2)]
  even = [x for x in range(2, pow(2,i)+1, 2)]
  arr2 = [x for x in range(1, pow(2,i) + 1)]
  arr = odd + even
  begin = time.perf_counter_ns()
  sortedArray = randomQuickSort(arr)
  end = time.perf_counter_ns()
  if sortedArray == arr2:
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data3.append(temp)

temp = ["Merge Sort"]
for i in range(5, 10):
  odd = [x for x in range(1, pow(2,i), 2)]
  even = [x for x in range(2, pow(2,i)+1, 2)]
  arr2 = [x for x in range(1, pow(2,i) + 1)]
  arr = odd + even
  begin = time.perf_counter_ns()
  mergeSort(arr)
  end = time.perf_counter_ns()
  if arr == arr2:
    temp.append(round(end-begin))
  else:
    temp.append("failed")
data3.append(temp)

res = data1 + [""] + data2 + [""] + data3
with open("result.csv", "w",encoding="utf-8", newline="") as file:
  writer = csv.writer(file)
  writer.writerows(res)