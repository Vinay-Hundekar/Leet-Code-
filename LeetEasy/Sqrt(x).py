class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=1
        while x//i>=i:
            i+=1
        return i-1
    
