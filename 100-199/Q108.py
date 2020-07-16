# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2;

        head = TreeNode(nums[mid])
        self.sortedArrayToBSTR(head, nums[:mid], nums[mid+1:])
        return head

    def sortedArrayToBSTR(self, head, left, right):
        if left:
            leftMid = len(left) // 2
            leftHead = TreeNode(left[leftMid])
            head.left = leftHead
            self.sortedArrayToBSTR(leftHead, left[:leftMid], left[leftMid+1:])
        if right:
            rightMid = len(right) // 2
            rightHead = TreeNode(right[rightMid])
            head.right = rightHead
            self.sortedArrayToBSTR(rightHead, right[:rightMid], right[rightMid+1:])

s = Solution()
nums = [-5, -2, 0, 4, 9]

a = s.sortedArrayToBST(nums)

print("end")
