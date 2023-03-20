class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # If low or high are odd
        # Count will should be incremented by one, because it is also included in count
        # Else just calculate the number between low and high and divide by 2  
        if low%2 or high%2:
            return (high-low)//2+1
        return (high-low)//2
             