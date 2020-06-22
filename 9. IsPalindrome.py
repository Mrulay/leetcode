class Solution:
    def isPalindrome(self, n: int) -> bool:
            if n<0:
                return False
            else: 
                rev = 0
                num = n
                while(num>0):
                    a = num%10
                    rev = (rev*10) + a 
                    num = num//10
                return n == rev