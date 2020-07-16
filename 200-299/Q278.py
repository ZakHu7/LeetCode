# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## binary search

        start, end = 1, n

        if isBadVersion(start):
            return start

        while start < end - 1:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        return end