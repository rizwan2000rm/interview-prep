def isAnagram(s, t):
    hashMap = {}

    if len(s) != len(t):
        return False

    for i in s:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1

    for i in t:
        if i not in hashMap:
            return False
        else:
            hashMap[i] -= 1

    for val in hashMap.values():
        if val != 0:
            return False

    return True
