class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Create an empty hashtable
        hashtable={}
        # Traversing through the nums
        # Using enumerate() function
        # Which will return index and values
        for ind, val in enumerate(nums):
            # Checking wether value is present in the hashtable
            # And difference between their index is lesser or equal to k
            # if so then return ture
            if val in hashtable and ind - hashtable[val] <= k:
                return True
            # Else add the value to hashtable,
            # Or update the index of value, if already present
            hashtable[val]=ind
        # Returning false if no duplicate is matching the constraints
        # Or all the elements are distinct
        return False