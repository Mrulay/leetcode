class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)-1
        i = 0
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last],nums[i]
                last -= 1
            else:
                i += 1
        return i
            