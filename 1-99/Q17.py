class Solution:

    mapping = [
        [],
        [],
        ["a","b","c"],
        ["d","e","f"],
        ["g","h","i"],
        ["j","k","l"],
        ["m","n","o"],
        ["p","q","r","s"],
        ["t","u","v"],
        ["w","x","y","z"],
    ]

    def letterCombinations(self, digits):
        if not digits:
            return []        
        return self.letterCombinationsR([""],digits)
    
    def letterCombinationsR(self, prefixes, digitsLeft):
        if digitsLeft == "":
            return prefixes

        newPrefixes = []
        for i in range(len(prefixes)):
            for letter in self.mapping[int(digitsLeft[0])]:
                newPrefixes.append(prefixes[i] + letter)
        
        return self.letterCombinationsR(newPrefixes, digitsLeft[1:])


s = Solution()
digits = "789"

print(s.letterCombinations(digits))