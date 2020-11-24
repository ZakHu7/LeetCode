def sortedMerge(a, sizea, b):
  end = len(a)-1
  endA = sizea-1
  endB = len(b)-1

  while end >= 0:
    if a[endA] > b[endB]:
      a[end] = a[endA]
      endA -= 1
    else:
      a[end] = b[endB]
      endB -= 1
    end -= 1

    if endA < 0:
      while endB >= 0:
        a[end] = b[endB]
        endB -= 1
        end -= 1



a = [2,5,7,8,9,0,0,0]
sizea = 5
b = [1,3,6]
sortedMerge(a, sizea, b)
print(a)


print(sorted(["bobs", "bob", "sbob", "boas"]))
print("".join(sorted("bobs")))