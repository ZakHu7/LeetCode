from collections import deque

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        found = deque()
        rest = {"total": 0}

        ## setup dictionary
        for c in s1:
            if c in rest.keys():
                rest[c] += 1
            else:
                rest[c] = 1
            rest["total"] += 1
        
        ## main iteration
        for c in s2:
            if c in rest.keys() and rest[c] != 0:
                rest[c] -= 1
                rest["total"] -= 1
                found.append(c)
            else:
                while found:
                    lastLetter = found.popleft()
                    if c == lastLetter:
                        found.append(c)
                        break
                    else:
                        rest[lastLetter] += 1
                        rest["total"] += 1
            if rest["total"] == 0:
                return True

        return False

s = Solution()
s1 = "b"
s2 = "aaabaaabaaaa"

print(s.checkInclusion(s1,s2))