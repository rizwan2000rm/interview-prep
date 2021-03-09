nums = [4,1,2,1,2]

hashSet = set()

for i in range(len(nums)):
  print(nums[i])
  if nums[i] in hashSet:
    hashSet.remove(nums[i])
    print(hashSet)
    
  hashSet.add(nums[i])
  print(hashSet)

print(hashSet.pop())
print(hashSet)