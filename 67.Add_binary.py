class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        result=[]
        carry=0
        while i>=0 or j>=0 or carry:
            sums=carry
            if i>=0:
             sums+=int(a[i])
            if j>=0:
             sums+=int(b[j])
            result.append(str(sums%2))
            carry= sums//2
            i-=1
            j-=1
        return ''.join(result[::-1])
    
"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""