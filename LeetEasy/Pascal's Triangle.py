class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #Initialy set output = [1] because oth index
        output=[1]
        #In pascals triange each and every values are nCr
        #Here we are calculating nCr with the help of previous value
        #Such as nCr = nCr-1 * (n-r+1)/r
        for i in range(1,rowIndex+1):
            output.append(output[i-1]*(rowIndex-i+1)/i)
        return output
