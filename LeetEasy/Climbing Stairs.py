class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1,n2,n3=1,1,1
        
        for i in range(1,n):
            n3=n1+n2
            n1=n2
            n2=n3
        return n3
    