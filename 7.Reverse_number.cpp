class Solution {
public:
    int reverse(int x) {
        const int MAX=2147483647;
        const int MIN=-2147483648;
        int rev=0;
        while (x!=0){
            int d=x%10;
            if(rev>MAX/10 || rev<MIN/10)
                return 0;
            if(rev==MAX/10 && d>7)
                return 0;
            if(rev==MIN/10 && d<-8)
                return 0;
            rev=rev*10+d;
            x=x/10;
        }
        return rev;
    }
};

/*
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
*/