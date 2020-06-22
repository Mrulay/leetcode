class Solution:
    def romanToInt(self, s: str) -> int:
        lis = []
        rome = {'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,
                'IV' : 4,
                'IX' : 9,
                'XL' : 40,
                'XC' : 90,
                'CD' : 400,
                'CM' : 900 }
        i = 0
        while i < (len(s)):
            t1 = s[i]
            t2 = s[i:i+2]
            if t2 in rome: 
                lis.append(rome[t2])
                i = i+2
            else:
                lis.append(rome[t1])
                i = i+1
        return (sum(lis))