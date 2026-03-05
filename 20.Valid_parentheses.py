class Solution:
    def isValid(self, s: str) -> bool:
        bracket=[]
        c={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in '({[':
                bracket.append(i)
            if i in ')}]':
                if len(bracket)==0:
                    return False
                elif bracket[-1]!=c[i]:
                    return False
                else:
                    bracket.pop()
        if len(bracket)==0:
            return True
        else:
            return False
        
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""