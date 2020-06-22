class Solution:
    def reverse(self, n: int) -> int:
            neg = False
            rev = 0
            if n<0: 
                n *= -1
                neg = True
            while(n>0):
                a = n%10
                rev = (rev*10) + a 
                n = n//10
            if neg == True:
                rev *= -1
            return rev if -pow(2,31) <= rev <= pow(2,31)-1 else 0 