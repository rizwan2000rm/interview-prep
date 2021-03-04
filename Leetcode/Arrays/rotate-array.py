class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverseArray(nums, 0, len(nums)-1)
        self.reverseArray(nums, 0, k-1)
        self.reverseArray(nums, k, len(nums)-1)

    def reverseArray(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
