# class Solution:
#     def threeSum(self, nums):
#         if len(nums) < 3:
#             return []
#         sortedNums = sorted(nums)
#         sol = []
#         first = 0
#         while first < len(sortedNums) - 2:
#             second = first + 1
#             third = len(sortedNums) - 1
#             while second < third:
#                 if sortedNums[first] + sortedNums[second] + sortedNums[third] == 0:
#                     sol.append([sortedNums[first], sortedNums[second], sortedNums[third]])
                    
#                     val = sortedNums[second]
#                     while sortedNums[second] == val and second < third:
#                         second += 1
#                     if second == third:
#                         break
#                     val = sortedNums[third]
#                     while sortedNums[third] == val and second < third:
#                         third -= 1
#                     if second == third:
#                         break
#                 elif sortedNums[first] + sortedNums[second] + sortedNums[third] < 0:
#                     val = sortedNums[second]
#                     while sortedNums[second] == val and second < third:
#                         second += 1
#                     if second == third:
#                         break
#                 elif sortedNums[first] + sortedNums[second] + sortedNums[third] > 0:
#                     val = sortedNums[third]
#                     while sortedNums[third] == val and second < third:
#                         third -= 1
#                     if second == third:
#                         break
#             val = sortedNums[first]
#             while sortedNums[first] == val and first < len(sortedNums) - 1:
#                 first += 1
#         return sol

class Solution():
  def threeSum(self, nums):
    res = {}
    if len(nums) < 3:
      return []
    
    nums.sort()
    lastNum = 1
    for i in range(len(nums)):
      if nums[i] > 0:
        break
      if nums[i] == lastNum:
          continue
      leftPointer, rightPointer = i+1, len(nums)-1
      while leftPointer < rightPointer:
        if nums[rightPointer] < 0:
            break
        if nums[leftPointer] + nums[rightPointer] == -nums[i]:
          sol = [nums[i], nums[leftPointer], nums[rightPointer]]
          res[str(sol)] = sol
          leftPointer += 1
          rightPointer -= 1
        elif nums[leftPointer] + nums[rightPointer] < -nums[i]:
          leftPointer += 1
        else:
          rightPointer -= 1
      lastNum = nums[i]
    return list(res.values())

s = Solution()

sortedNums = [-1, 0, 1, 2, -1, -4]
sortedNums = [0,0]
sortedNums = [-5,6,-2,-4]

print(s.threeSum(sortedNums))
#🙃🙃🙃
