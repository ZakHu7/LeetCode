from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: [int]) -> str:
        strNums = list(map(str, nums))

        def compare(a: str, b: str) -> int:
            return 1 if int(a + b) > int (b + a) else -1

        strNums.sort(key=cmp_to_key(compare), reverse=True)

        ret = "".join(strNums)

        return "0" if strNums[0] == "0" else ret

s = Solution()
nums = [0, 0]

print(s.largestNumber(nums))