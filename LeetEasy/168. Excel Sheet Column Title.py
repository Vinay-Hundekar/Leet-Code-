class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        #String which represents Column Title
        ans=''
        
        while columnNumber>0:
            #Decrementing the columnNumber so that we can get the index
            #value when we take mod of columnNumber
            columnNumber -= 1

            #Adding mod with 65 to gert the ASCII value of the number
            #By thaking mod, we get character in reverse order, means last character of the title first
            #So we use ans= new charcter + ans
            ans=chr(columnNumber%26 + 65) + ans

            #Than floor divide the colmnNumber to get the next character
            columnNumber//=26

        #Return the obtained answer
        return ans