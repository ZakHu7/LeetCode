class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    biggest = float('-inf')
    ind = -1
    for i in range(len(nums)-1, -1, -1):
      if nums[i] < biggest:
        ind = i
        break
      else:
        biggest = nums[i]
    
    if ind != -1:
      for j in range(len(nums)-1, ind, -1):
        if nums[j] > nums[ind]:
          nums[j], nums[ind] = nums[ind], nums[j]
          break
    ind += 1
    for k in range((len(nums)-ind)//2):
      nums[ind+k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[ind+k]