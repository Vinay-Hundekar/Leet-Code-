class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c=0
        m=len(s) # Length of the subsequence
        # Checking wether the subsequence is empty
        # If so then return True
        if c==m:
            return True
        for i in t:
            # If element of t in s then increment the index (c) by one
            if i==s[c]:
                c+=1
            # Checking wether the index value is equal to length of the subsequence
            # If so then return True
            if c==m:
                return True
        return False