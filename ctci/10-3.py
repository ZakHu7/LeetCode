def searchRotateArr(arr, n):
  low = 0
  high = len(arr)-1

  while low <= high:
    mid = low + (high-low)//2

    if arr[low] < arr[mid]:
      if arr[low] <= n < arr[mid]:
        high = mid-1
      elif n < arr[low] or n > arr[mid]:
        low = mid+1
      else:
        return mid
    elif arr[low] > arr[mid]:
      if n >= arr[low] or n < arr[mid]:
        high = mid-1
      elif n > arr[mid]:
        low = mid+1
      else:
        return mid
    else: return mid

  return -1

arr = [15,16,19,20,25,1,3,4,5,7,10,14]
print(searchRotateArr(arr, 15))

## what about duplicate? search both sides

