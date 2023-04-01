class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Lower bound
        l=0
        # Upper bound
        h=len(nums)-1
        while(l<h):
            # Calculating mid
            mid=(l+h)//2
            # Checking wether target is present at mid
            if nums[mid]==target:
                return mid
            # If target is lesser than mid than seting upper bound as mid-1
            elif nums[mid]> target:
                h=mid-1
            # Else target is greater than mid than seting lower bound as mid+1
            else:
                l=mid+1
        # Checking wether target is present at lower bound, cause lower and upper bound are equal
        # If so than return lower bound
        if nums[l]==target:
            return l
        # Else return -1, which indicate element is not present
        return -1
