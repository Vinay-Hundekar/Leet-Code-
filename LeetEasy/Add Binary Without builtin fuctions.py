class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b)>len(a):
            b,a=a,b

        c=0
        s=''
        for i,j in zip(a[::-1],b[::-1]):
            if c==1:
                if i=='1' and j=='1':
                    s+='1'
                    c=1
                elif i=='1' or j=='1':
                    s+='0'
                    c=1
                else:
                    s+='1'
                    c=0
            else:
                if i=='1' and j=='1':
                    s+='0'
                    c=1
                elif i=='1' or j=='1':
                    s+='1'
                    c=0
                else:
                    s+='0'
                    c=0
        b=len(b)+1


        for i in a[-b::-1]:
            if c==1:
                if i=='1':
                    s+='0'
                    c=1
                else:
                    s+='1'
                    c=0
            else:
                s+=i
        if c==1:
            s+='1'
        return s[::-1]
