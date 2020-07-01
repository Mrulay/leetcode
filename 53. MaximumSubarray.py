class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm 
        cur_max = glob_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i]+cur_max)
            if cur_max > glob_max:
                glob_max = cur_max
        return glob_max
    
    def maxSubArray2(self, nums: List[int]) -> int:
        #Better Kadane's Algorithm
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)