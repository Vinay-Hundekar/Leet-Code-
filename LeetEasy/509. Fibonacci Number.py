class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # In fibonacci number
        # F(0) = 0, F(1) = 1
        if n in [0,1]:
            return n

        n1=0
        n2=1
        # F(n) = F(n - 1) + F(n - 2), for n > 1.
        # Or n3=n2+n1
        n3=n1+n2
        # Itirate till n-2 times beacause we already know the value of first two fibonacci number
        for i in range(n-2):
            n1=n2
            n2=n3
            n3=n1+n2
        # Return the fibonacci number
        return n3