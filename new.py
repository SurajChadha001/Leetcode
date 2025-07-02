class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        W = int(math.sqrt(area))
        while area % W != 0:
            W -= 1
        L = area // W
        return [L, W]