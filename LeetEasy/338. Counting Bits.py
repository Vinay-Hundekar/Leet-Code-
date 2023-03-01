class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #Initializing list 0th index a zero
        ans=[0]
        for i in range(1,n+1):
            #i>>1 gives the half of the number
            #And the number of 1's in a number is same as its half if its even number
            #else if the number is odd then increment by 1
            #so i%2 is used
            #Hence it uses its previous data.
            #So it belongs to Dynamic Programing Caagory.
            ans.append(ans[i>>1] + i%2)
        return ans