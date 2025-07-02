class Solution(object):
    def hammingDistance(self, x, y):

        xor = x ^ y
        distance = 0
        while xor:
            distance += xor & 1
            xor >>= 1
        return distance