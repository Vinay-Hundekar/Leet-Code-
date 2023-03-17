class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # First we check wether n is +ve integer or not
        # If n is -ve integer then return False, which act as base case
        if n<=0:
            return False
        # Checking wether n==1, which is base case
        # It indicates that n is power of 3
        elif n==1:
            return True
        # Checking wether n it perfectly divisible by 3
        # If so than recursing by passing n//3 as argument 
        elif n%3==0:
           return self.isPowerOfThree(n//3)
        # If n is not divisible by 3 than return False
        return False