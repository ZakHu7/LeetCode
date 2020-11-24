def groupAnagrams(arr):
  numChars = countCharsInArr(arr)
  groupAnagramsH(numChars)


def groupAnagramsH(numChars):
  for i in range(26):
    countSort(numChars, i)

def countSort(numChars, i):
  res = len(numChars) * []


def countCharsInArr(arr):
  res = []
  for i in range(len(arr)):
    numCharsInStr = countCharsInStr(arr[i])
    res += numCharsInStr
  return res

def countCharsInStr(s):
  res = [0]*26
  for i in range(len(s)):
    c = ord(s[i].lower()) - ord('a')
    res[c] += 1
  return res
