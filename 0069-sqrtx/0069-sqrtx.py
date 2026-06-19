class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0

        while (i + 1) * (i + 1) <= x:
            i += 1

        return i