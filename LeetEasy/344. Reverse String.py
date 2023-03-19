class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.

        Pythonic solution
        s[:]=s[::-1]
        """
        # Find the middle index and swap the 1st and last index element
        for i in range(len(s)//2):
            s[i],s[-1-i]=s[-1-i],s[i]