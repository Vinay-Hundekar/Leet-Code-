class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Converting the given list into set
        s1=set(nums)
        # Creating the another set of expected value
        s2=set(range(len(nums)+1))
        # Subtracting the s2 by s1 gives us the element present in s2 but not in s1
        # Which is the required value, and poping it gives us integer
        # So no need to type caste
        return (s2-s1).pop()

        # calculate expected sum of numbers in the list
        expected_sum = len(nums) * (len(nums) + 1) // 2
        # Calculating the given list sum
        actual_sum = sum(nums)
        # Subtaracting the expected_sum by actual_sum gives us the missing number
        return expected_sum - actual_sum