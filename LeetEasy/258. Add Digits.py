class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Loop until the num is single digit
        while num > 9:
            num=self.sumofdigits(num)
        return num
    # Function to add the digits of number
    def sumofdigits(self,num):
        sum=0
        while num!=0:            
            sum+=num%10
            num//=10
        return sum