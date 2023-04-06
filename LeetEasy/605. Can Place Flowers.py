class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # If length of the flowerbed is one, it can only have one flower
        if len(flowerbed)==1:
            return True if( flowerbed[0]==0 and n<=1) or n==0 else False
        # If starting two pots are empty, than first pot can be planted with flower
        if flowerbed[:2]==[0,0]:
            flowerbed[0]=1
            n-=1
        i=1
        while i<len(flowerbed)-1:
            # Checking if previous pot, current pot, and next pot are empty 
            # If so than plant the flower at current position
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            i+=1
        # If last two pots are empty, than lastt pot can be planted with flower
        if flowerbed[-2]==0 and flowerbed[-1]==0:
            flowerbed[-1]=1
            n-=1
        # Return if if it is posible to plan n new flowers
        return False if n>0 else True