class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s=re.findall('[A-Za-z0-9]',s.lower())
        return True if s==s[::-1] else False