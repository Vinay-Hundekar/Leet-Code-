class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # You can always win a Nim game 
        # if the number of stones in the pile is not divisible by 4.
        return n%4