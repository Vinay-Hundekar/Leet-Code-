class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Traverse through each element and add it with its previous element
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        #return the nums
        return nums