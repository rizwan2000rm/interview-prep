class Solution:
    def isPalindrome(self, s):
        beg, end = 0, len(s) - 1
        while beg <= end:
            while not s[beg].isalnum() and beg < end:
                beg += 1
            while not s[end].isalnum() and beg < end:
                end -= 1
            if s[beg].lower() == s[end].lower():
                beg, end = beg + 1, end - 1
            else:
                return False
        return True
