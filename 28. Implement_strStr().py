class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack=="" and needle=="": 
            return 0
        nedLen = len(needle)
        for i in range(len(haystack)):
          new = haystack[i:nedLen]
          nedLen += 1
          if new==needle:
            return (i)
        return -1
            
        