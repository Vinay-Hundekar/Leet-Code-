class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        # Counting the number of zeros
        # Removing them from nums and appending( inserting at the end) it to nums        
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        """
        # Index to traverse through nums and find non zero values
        i=0
        # Index to point zero value
        j=0
        # Loop until nums is completly traversed
        while i<len(nums):
            # If i th index points to non zero value
            # Swap with the j th index, which points zero
            if nums[i] != 0:
                nums[i], nums[j]=nums[j], nums[i]
                # Incrementing j th value
                j+=1
            # Incrementing i th value
            i+=1