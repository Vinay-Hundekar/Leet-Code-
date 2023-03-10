class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Set to store the calculated sum of sequence of digits in n
        calculated={n}
        while n!=1:
            # sum(n) will return the sum of sequence of digits in n
            n=self.sum(n)
            # Checking wether the sum is repeted
            # If so return False
            if n in calculated:
                return False
            # Adding the new number obtained to calculated set
            calculated.add(n)
        # Returning True if n == 1
        return True

    # Function to calculate sum of sequence of digits in n 
    def sum(self,n):
        # Initializing sum of n(sumfn) to zero
        sumofn=0
        while n != 0:
            # Calculating square of each a every digits in n 
            # And adding it to sum of n(sumfn)
            sumofn+=(n%10)**2
            n//=10
        # Returning the sum of n
        return sumofn
            
