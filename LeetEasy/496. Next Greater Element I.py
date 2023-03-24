class Solution(object):
    def ans(self,i,nums,x):
        while i<len(nums)-1:
            if nums[i+1]>x:
                return nums[i+1]
            i+=1
        return -1


    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums1)):
            nums1[i]=self.ans(nums2.index(nums1[i]),nums2,nums1[i])
        return nums1