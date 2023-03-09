class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Variable to count number of 1's
        count=0

        # Loopp until n is equal to zero
        while n:
            # This exprestions equates n to n-1 or zero
            n&=(n-1)
            # Increment the counter
            count+=1
        # Return the number of 1's
        return count