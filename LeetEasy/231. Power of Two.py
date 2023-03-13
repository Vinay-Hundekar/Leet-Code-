class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

       # Simple brutforce solution
        for i in range(32):
            if n == 2**i:
                return True
        return False

        # Solution using bitwise right shift operater
        while n != 1 :
            if n%2 != 0 or n==0:
                return False
            n>>=1
        return True
        """
        # if n is equal to zero hen its not the power of two
        # And if n is power of two
        # Than it will give zero if n is bitwise anded with n-1 
        # Else some other number
        # Example 8=1000, 7=111, 1000 & 0100 = 0000
        # Example two 6= 110 , 5=101 , 110 & 101 =100 
        return (n != 0) and (n & (n-1) == 0)