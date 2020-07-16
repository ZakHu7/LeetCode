class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        sol = []
        numsSorted = sorted(nums)
        start = 0
        end = len(numsSorted) - 1

        while start + 1< end:
            lookingFor = -(numsSorted[start] + numsSorted[end])

            if lookingFor < 0:
                for i in range(start + 1, end):
                    if lookingFor < numsSorted[i]:
                        break
                    if lookingFor == numsSorted[i]:
                        sol.append([numsSorted[start],numsSorted[i],numsSorted[end]])
                        break
                end -= 1

                while end >= 0 and numsSorted[end + 1] == numsSorted[end]:
                    end -= 1

            elif lookingFor > 0:
                for i in range(end - 1, start, -1):
                    if lookingFor > numsSorted[i]:
                        break
                    if lookingFor == numsSorted[i]:
                        sol.append([numsSorted[start],numsSorted[i],numsSorted[end]])
                        break
                start += 1

                while start < len(numsSorted) and numsSorted[start - 1] == numsSorted[start]:
                    start += 1
            else:
                for i in range(end - 1, start, -1):
                    if lookingFor == numsSorted[i]:
                        sol.append([numsSorted[start],numsSorted[i],numsSorted[end]])
                        break
                if numsSorted[end - 1] + numsSorted[start + 1] < 0:
                    start += 1
                    while start < len(numsSorted) and numsSorted[start - 1] == numsSorted[start]:
                        start += 1
                elif numsSorted[end - 1] + numsSorted[start + 1] < 0:
                    end -= 1
                    while end >= 0 and numsSorted[end + 1] == numsSorted[end]:
                        end -= 1
                else: break


        return sol

s = Solution()

nums = [-1, 0, 1, 2, -1, -4]
nums = [-2,-1,-1,0,1,2]

print(s.threeSum(nums))


         