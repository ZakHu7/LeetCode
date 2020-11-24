import random

def quickSort(arr, left, right):
  pivotInd = partition(arr, left, right)

  if left < pivotInd - 1:
    quickSort(arr, left, pivotInd-1)
  if right > pivotInd + 1:
    quickSort(arr, pivotInd+1, right)

def partition(arr, left, right):
  pivotInd = right
  pivot = arr[pivotInd]
  right -= 1

  while left <= right:
    while arr[left] < pivot:
      left += 1
    while arr[right] > pivot:
      right -= 1
    
    if left <= right:
      arr[left], arr[right] = arr[right], arr[left]

  arr[left], arr[pivotInd] = arr[pivotInd], arr[left]

  return left




arr = list(range(10))
random.shuffle(arr)
print(arr)
quickSort(arr, 0, len(arr)-1)

print(arr)