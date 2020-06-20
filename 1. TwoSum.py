def twoSum(nums, target):
        d = dict()
        for i,n in enumerate(nums):
            m = target - n 
            if m not in d:
                d[n] = i
            else:
                return [d[m], i]
        
x = twoSum([2,7,11,10], 9)
print (x)