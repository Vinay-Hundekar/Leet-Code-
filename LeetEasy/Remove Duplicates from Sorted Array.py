class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=[]
        j=0
        for  i in nums:
            if i not in k:
                k.append(i)
                nums[j]=i
                j+=1
        return len(k)