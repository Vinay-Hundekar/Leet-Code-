class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # If number is zero it doesnot have prime factors
        if n ==0:
            return False
        # Vaild prime factors for a number to be a ugly number
        pnumber=[2,3,5]
        # i represents the index value of pnumber
        i=0
        # Looping until a number becomes one or i is greater then 2
        while n != 1:
            # Checking wether the number is divisible by pnumber
            if n % pnumber[i] ==0:
                n//=pnumber[i]
                continue
            # If not incrementing i by one
            i+=1
            # Checking if index value does not excedes the length of the list
            # If so return False
            if i>2:
                return False
        return True

   