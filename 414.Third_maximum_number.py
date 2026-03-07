class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=b=c=float('-inf')
        for i in nums:
            if i==a or i==b or i==c:
                continue
            if i>a:
                c=b
                b=a
                a=i
            elif i>b:
                c=b
                b=i
            elif i>c:
                c=i
        if c!=float('-inf'):
            return c
        else:
            return a

"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""