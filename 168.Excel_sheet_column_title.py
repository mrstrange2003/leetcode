class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num=columnNumber
        char=""
        while num>0:
            num-=1
            last=num%26
            char=chr(65+last)+char
            num=num//26
        return char
    
"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 2^31 - 1
"""