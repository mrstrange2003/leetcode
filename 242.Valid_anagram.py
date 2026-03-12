class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        n=len(s)
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]]=1
            else:
                dic[s[i]]+=1           
        for i in range(n):
            if t[i] not in dic:
                return False
            else:
                dic[t[i]]-=1
                if dic[t[i]]<0:
                    return False
        return True
        

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""