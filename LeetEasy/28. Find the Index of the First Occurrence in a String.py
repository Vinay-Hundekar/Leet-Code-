class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Checking wether the needle is present in haystack
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)):
            # c is a variable to hold the index value of heystack
            # to compare with needle
            c=i

            # flag to check the occurence of needle
            flag=1

            for j in needle:
                if j != haystack[c]:
                    # If character don't match then turn flag to 0 and break
                    flag=0
                    break
                # Incrementing the haystack index
                c+=1
            # Checking wether needle is present in haystack   
            if flag == 1:
                break
        # returning the index of the first occurrence
        return i
        

        
        # The find() method finds the first occurrence of the specified value. 
        # The find() method returns -1 if the value is not found.
        # return haystack.find(needle)
        # Even you can use index() to find, 
        # it will raises an exception if the value is not found.
        # return haystack.index(needle)
