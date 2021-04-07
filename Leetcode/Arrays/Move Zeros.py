class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in nums:
            if(i != 0):
                nums[pointer] = i
                pointer += 1

        for i in range(pointer, len(nums)):
            nums[i] = 0
