class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target<nums[0]:
            return 0
        mx=len(nums)-1
        mn=0
        while mn<mx:
            md=(mn+mx)/2
            if nums[md]==target:
                return md
            elif nums[md]>target:
                mx=md-1
            else:
                mn=md+1
        if mn==mx:
            if nums[mn]>target or target==nums[mn]:
                return mn
            else:
                return mn+1
        return md