class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=0
        for i in digits:
            n=n*10+i
        digits=[]
        n+=1
        while n!=0:
            r=n%10
            n//=10
            digits.append(r)
        return digits[::-1]