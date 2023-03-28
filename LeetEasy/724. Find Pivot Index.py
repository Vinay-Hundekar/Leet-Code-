class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initializing left sum as 0 and right sum as total sum
        left,reight=0,sum(nums)
        for i in range(len(nums)):
            # Checking wether left sum is equal to right sum subtracted by current element
            # If so then it is a pivot element
            if left==reight-nums[i]:
                return i
            # If not add the current element to left sum
            left+=nums[i]
            # And subtract the right sum by current element
            reight-=nums[i]
        # If pivot is not found than return -1
        return -1        
