class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        #To calculate the Column Number initialize columnNumber to zero
        columnNumber=0
        #Power helps us to calculate the value to character in the perticular position
        #Each carecters numeric value is equal to index multiplied by 26 rised to power value
        #Example ZY = 701
        #Z power value = 1, and index value = 26, 26 * 26 = 676
        #Y power value = 0, and index value = 25, 25 *1 = 25
        #and then add then 676 + 25 = 701

        power=len(columnTitle)-1
        for i in columnTitle:
            # ord() gives ASCII value and -64 gives index value of the caracter
            columnNumber+=(ord(i)-64)*(26**power)
            #To decrement the power value
            power-=1
        return columnNumber