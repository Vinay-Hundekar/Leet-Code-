class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # WE ARE SOLVING THIS PROBLEM WITH THE HELP OF
        #       RECURSION AND BITMANUPULATON
        # Checking wether n==1, because 4^0=1, than return True
        if n==1:
            return True
        # IF n==0 , return False
        elif n=0:
            return False
        # If n is multipule of 4, than perform n>>2(bitmanipulation)
        # because n>>2 is same as n//4, but faster
        # And than do recursion
        elif n%4==0:
            return self.isPowerOfFour(n>>2)
        # If the number is not divisible by four return False
        return False