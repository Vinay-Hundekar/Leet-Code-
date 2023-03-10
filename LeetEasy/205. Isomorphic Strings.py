class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Dictionary to keep track of charcter apping
        d={}
        for i,j in zip(s,t):
            # Checking wether charecter in s is mapping to other charecter in t
            if i in d and d[i] != j:
                return False 
            # Checking wether charecter in t is already mapped to some other charecter of s
            elif i not in d and j in d.values():
                return False 
            # Mapping a charecter of s to charecter of t       
            d[i]=j
        return True