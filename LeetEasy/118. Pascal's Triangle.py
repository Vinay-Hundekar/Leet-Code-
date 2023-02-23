class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]

        result=[[1],[1,1]]
        for i in range(numRows-2):
            current=[1]
            for i in range(1,len(result[-1])):
                current.append(result[-1][i-1]+result[-1][i])
            current.append(1)
            result.append(current)
        return result