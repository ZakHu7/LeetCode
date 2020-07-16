class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        check = len(digits) - 1

        while check >= 0:
            digits[check] += 1

            if digits[check] == 10:
                digits[check] %= 10
                check -= 1
            else:
                return digits
        digits.insert(0,1)
        return digits


s = Solution()
digits = [9,9]
print(s.plusOne(digits))