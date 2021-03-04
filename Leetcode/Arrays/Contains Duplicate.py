class Solution:
    def containsDuplicate(self, nums):
        hashSet = set()
        for i in range(len(nums)):
            if(nums[i] in hashSet):
                return True
            hashSet.add(nums[i])
        return False
