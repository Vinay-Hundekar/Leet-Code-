class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        n1=0
        n2=0
        new=nums1[:m]
        if n==0:
            nums1=nums1
        else:
            for i in range(len(nums1)):
                if n1==m:
                    nums1[i]=nums2[n2]
                    n2+=1
                elif n2==n:
                    nums1[i]=new[n1]
                    n1+=1
                    
                else:
                    if new[n1]<nums2[n2]:
                        nums1[i]=new[n1]
                        n1+=1
                    else:
                        nums1[i]=nums2[n2]
                        n2+=1

