class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If length of s and t are not equal than they are not Anagram
        if len(s) != len(t):
            return False
        # Creating empty dictionary to keep track of characters of s
        dic={}
        # Traversing through s for character and updating there count as key and values respectively in dictionary
        for i in s:
            # If caracter is not present dictionary, seting its count to zero
            dic.setdefault(i,0)
            # If character is present in dictionary, incrementing its count by one
            dic[i]+=1
        # Traversing through t              
        for i in t:
            # Checking if character of t is not in dictionary or count of character is zero
            # if so than return False
            if i not in dic or dic[i]==0:
                return False
            # Decrementing the count of caracter if it is present in dictionary
            dic[i]-=1
        return True