class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialy result will be zero
        result = 0
        for num in nums:
            # We take exor or each number
            # Because exor a number gives
            # Sum if a number is exored with a number lesser than it
            # Absolute difference if a number is exored with a number greater than it
            # Zero if exored with same number
            # Hence when a list number which has all the element repeted twice except one
            # is exored then it will give us the element which is distinct in the list
            result ^= num        
        # Return the obtained value
        return result
            