class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if d[s[i+1]]>d[s[i]]:
                sum-=d[s[i]]                
                continue
            sum+=d[s[i]]            
        sum+=d[s[len(s)-1]]
        return sum
            