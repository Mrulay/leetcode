class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        res = ""
        for i in range(n-1):
            s += "*"
            res = ""
            count = 1
            for j in range(1, len(s)):
                if s[j-1] != s[j]:
                    res += str(count)
                    res += s[j-1]
                    count = 1
                else:
                    count += 1
            s = res 
        return (s)
        