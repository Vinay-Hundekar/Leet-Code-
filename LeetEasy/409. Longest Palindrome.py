class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Creating dictionary  to note the frequency of characters
        d={}
        for i in s:
            # If character is not present in dictionary setting its values as 0
            d.setdefault(i,0)
            # And incrementing count by one 
            d[i]+=1
        # Varable to determine length
        total=0
        # Varable to check wether odd number is present or not
        c=0
        for i in d:
            # If character count in dictionary is odd
            # Than add the count-1 to total and set c as 1
            if d[i]%2:
                total+=(d[i]-1)
                c=1
                continue
            # Else add the count to tatal
            total+=d[i]
        # Retrun total+c if odd number of character is present c will be one else zero
        return total+c