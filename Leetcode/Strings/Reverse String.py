def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)//2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
