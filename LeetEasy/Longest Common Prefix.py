class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prf=strs[0]
        for a in strs:
            i=0
            while i != len(a) and i != len(prf):
                if prf[i]==a[i]:
                    i+=1
                else:
                    break
            prf=prf[:i]
        return prf