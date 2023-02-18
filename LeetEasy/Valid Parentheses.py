class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0] in ')}]':
            return False
        out=s[0]

        for i in range(1,len(s)):
            if s[i] not in ')}]':
                out+=s[i]
                continue
            elif out=="":
                return False        
            elif s[i]==')' and '(' ==out[-1]:
                out=out[:-1]
                continue
            elif s[i]==']' and '[' ==out[-1]:
                out=out[:-1]
                continue
            elif s[i]=='}' and '{' ==out[-1]:
                out=out[:-1]
                continue
            else:
                return False
            
        if out=="":
            return True
        return False