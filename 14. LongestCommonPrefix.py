class Solution:
    def LCPHelper(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        res = ""
        i,j = 0,0
        while i < l1 and j < l2:
            if str1[i] != str2[j]:
                break
            else:
                res += str1[i]
                i += 1
                j += 1
        return res
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: 
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            pref = strs[0]

            for m in range(1, len(strs)):
                pref = self.LCPHelper(pref, strs[m])

            return pref