class Solution:
    dic = {"[":"]",
    "{":"}",
    "(":")"}
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s: 
            if i in self.dic: 
                stack.append(i)
            elif not stack:
                return False
            else:
                a = stack.pop()
                if self.dic[a]!=i:
                    return False 
        return (True if len(stack)==0 else False)
