class Solution(object):
    # Function to delete charcter before '#'
    def stack(self,s):
        snew=[]
        for i in s:
            # If the character is # and stack is not empty
            # than pop the top character
            if i=='#':
                if snew:
                    snew.pop()
            # Else append the character to stack
            else:
                snew.append(i)
        # Return the stack
        return snew

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Return True if stack of s and t are same
        # Else return False
        return self.stack(s)==self.stack(t)