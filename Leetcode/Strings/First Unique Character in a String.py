def firstUniqChar(self, s: str):
    count = {}

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1
