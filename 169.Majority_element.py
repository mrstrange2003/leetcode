class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=0
        count=0
        for i in nums:
            if count==0:
                majority=i
            if i==majority:
                count+=1
            else:
                count-=1          
        return majority

            
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
The input is generated such that a majority element will exist in the array.
"""