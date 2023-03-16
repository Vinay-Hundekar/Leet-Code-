class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Initializing self.nums means cuurent object nums to nums
        self.nums=nums
        # Doing prefix sum, so that when a sumRange function is called
        # Exicution will be easier and fast
        for i in range(len(nums)-1):
            # Adding previous number to current number
            # Prefix Sum
            self.nums[i+1]+=nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # if left == 0, than nums[right] will have the sum of elements
        # else we should subtact the nums[right] by nums[left-1]
        # Because we only need sum from left to right
        # So we should subtract total sum(nums[right]) by sum of elements from 0 to left-1
        return self.nums[right]-self.nums[left-1] if left else self.nums[right]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)