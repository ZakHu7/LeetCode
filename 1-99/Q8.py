class Solution():
  def atoi(self, s):
    neg = 1
    res = 0

    s = s.strip()
    if len(s) == 0:
      return res
    if s[0] == '-':
      neg = -1
      s = s[1:]
    elif s[0] == '+':
      s = s[1:]
    for c in s:
      if c.isdigit():
        res = res * 10 + int(c)
      else:
        return res
    return res * neg

s = Solution()
s1 = "42"
print(s.atoi(s1))

s1 = "    -42"
print(s.atoi(s1))

s1 = "4193 with words"
print(s.atoi(s1))

s1 = "words and 987"
print(s.atoi(s1))

s1 = "-91283472332"
print(s.atoi(s1))

s1 = "  "
print(s.atoi(s1))