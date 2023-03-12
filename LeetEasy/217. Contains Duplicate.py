class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Using inbuilt functions

        new=set(nums)
        return len(new) != len(nums)
        """
        # Creating the dectionary to keep record of number and its count
        hashtable={}
        # If number a already present in hashtable then its is dublicate
        # Hence return true
        for i in nums:
            if i in hashtable:
                return True
            # Adding numbers to hashtable if it is not present in it
            hashtable[i]=1
        # If no duplicate is found return false
        return False