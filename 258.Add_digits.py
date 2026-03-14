class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        else:
            return (num-1)%9+1
        

class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while num>9:
            sums=0
            while num>0:
                dig=num%10
                sums+=dig
                num//=10
            if sums<=9:
                return sums
            num=sums

            
'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 2^31 - 1
'''