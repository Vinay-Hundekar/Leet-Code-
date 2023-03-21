class Solution {
public:
    int subtractProductAndSum(int n) {
        //Initializing product and sum variable tp 1 and 0 respectivly
        int p=1,s=0;
        // Looping until n is not equal to zero
        while(n!=0)
        {
            // taking remainder(n%10) and multiplying with product and adding with sum
            // and dividing the n by 10
            p*=n%10;
            s+=n%10;
            n/=10;
        }
        // Returning the product - sum
        return p-s;
        
    }
};