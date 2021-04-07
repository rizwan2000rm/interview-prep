class Solution:
    def plusOne(self, digits):

        sum = 0
        for i in digits:
            sum = sum * 10 + i
            print(sum)
        sum += 1

        return [int(i) for i in str(sum)]
