class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        s1, s2 = 0, 0
        e1, e2 = len(nums1) - 1, len(nums2) - 1

        kBeforeTarget = (len(nums1) + len(nums2) + 1)//2 - 1 #for now only consider when sum of both lists are odd

        while(s1 <= e1 and s2 <= e2):
          m1, m2 = (s1 + e1)//2, (s2 + e2)//2

          if nums1[m1] < nums1[m2]:
            kBefore1 = m1 + 1
            kBefore2 = m2
            if kBefore1 + kBefore2 < kBeforeTarget:
              s2 = m2 + 1
            elif kBefore1 + kBefore2 == kBeforeTarget:
              s1 = m1 + 1
            elif kBefore1 + kBefore2 > kBeforeTarget:
              e2 = m2 - 1
          elif nums1[m1] >= nums1[m2]:
            kBefore1 = m1
            kBefore2 = m2 + 1
            if kBefore1 + kBefore2 < kBeforeTarget:
              s1 = m1 + 1
            elif kBefore1 + kBefore2 == kBeforeTarget:
              s2 = m2 + 1
            elif kBefore1 + kBefore2 > kBeforeTarget:
              e1 = m1 - 1
