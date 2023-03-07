class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #integer to store reverse bits
        reverse=0
        for i in range(32):
            # Left shifting the reverse by one bit
            # and adding n&1(Which will give either 0 or 1)
            reverse=(reverse<<1)+(n&1)
            # Right shifting the n by one bit
            n>>=1
        return reverse