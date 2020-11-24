def binSearchR(arr, n, left, right):
  ##arr is sorted
  if left >= right:
    return -1
  ind = left + (right - left)//2
  mid = arr[ind]
  if n < mid:
    return binSearchR(arr,n,left,ind-1)
  if n > mid:
    return binSearchR(arr,n,ind+1,right)
  if n == mid:
    return ind

def binSearch(arr, n):
  low = 0
  high = len(arr)-1

  while low <= high:
    mid = low + (high-low)//2
    if n < arr[mid]:
      high = mid - 1
    elif n > arr[mid]:
      low = mid + 1
    else: return mid
  return -1



arr = [1,2,6,9,34,57,76,87,88,100]

print(binSearch(arr,1))