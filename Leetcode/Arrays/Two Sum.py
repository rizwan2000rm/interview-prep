def twoSum(self, nums, target):
    hashMap = {}
    for i in range(len(nums)):
        combineWith = target - nums[i]

        if combineWith in hashMap:
            return [hashMap[combineWith], i]
            
        hashMap[nums[i]] = i
