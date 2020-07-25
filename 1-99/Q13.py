class Solution:
  def romanToInt(self, s: str) -> int:

    numbers = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    ## what i missed:
    ##  no need for extra case when i = len(s) - 1. Do it in the beginning
    ##  instead of checking every case separately (I followed by V,X...), one check "numbers[first] < numbers[second]"
    ##  still same runtime O(n), space O(number of symbols)

    retval = numbers[s[-1]]

    i = 0
    while (i < len(s) - 1):
      first, second = s[i], s[i+1]
      if numbers[first] < numbers[second]:
        retval -= numbers[first]
      else:
        retval += numbers[first]
      
      i += 1
    return retval

sol = Solution()
s = "MCMXCIV"
print(sol.romanToInt(s))
      