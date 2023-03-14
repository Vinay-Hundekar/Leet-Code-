# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using Binary search
        # Initializing the minimum value to 1 and maximum value to n
        minimum=1
        maximum=n
        # Calculating the mid(middle) value
        mid=(minimum+maximum)//2
        # Looping until minimum is lesser than maximum
        while minimum<maximum: 
            # if mid is badversion than updating maximum value to mid-1
            # Because we should searchin on the left side           
            if isBadVersion(mid):
                maximum=mid-1
            # else updating minimum value to mid+1
            # Because we should searchin on the right side
            else:
                minimum=mid+1
            # Again calculating mid value since minimum or maximum value are updated
            mid=(minimum+maximum)//2
        # Checking wether mid is bad version, if so return it
        if isBadVersion(mid):
            return mid
        # Else return mid+1, because it should be bad version
        return mid+1