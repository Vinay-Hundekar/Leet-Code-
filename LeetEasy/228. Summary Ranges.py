class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Checking wether array is empty, 
        # if so, than return the same
        if nums==[]:
            return nums
        # Initializing a(Start of range) and b(end of range) to nums[0]
        a=nums[0]
        b=a
        # Initializing ranges to empty list
        # ranges list is to store output ranges 
        ranges=[]
        for i in range(1,len(nums)):
            # To check wether the numbers are in sequence
            # if so the update the b value which is the end of the range             
            if nums[i]-nums[i-1]==1:
                b=nums[i]
            else:
                # If not then check wether a and b are equal
                # If equal then append only a as string
                if a == b :
                    ranges.append(str(a))                     
                else:
                    # Else append a->b 
                    ranges.append(str(a)+'->'+str(b))
                # Updating the a
                # Now it will represent start of next range  
                a=nums[i]
                # And also b
                b=a
        # Checking the last last value of nums(b)
        if a==b:
            ranges.append(str(a))
        else:
            ranges.append(str(a)+'->'+str(b))
        # Returning the list of ranges
        return ranges