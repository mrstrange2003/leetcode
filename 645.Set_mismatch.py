class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        realsum=sum(nums)
        expectedsum= len(nums)*(len(nums)+1)//2
        numset=set(nums)
        setsum=sum(numset)
        missing=expectedsum-setsum
        duplicate=realsum-setsum
        return [duplicate,missing]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(1,len(nums)+1):
            if dic.get(i,0)==2:
                duplicate=i
            if dic.get(i,0)==0:
                missing=i
        return [duplicate,missing]
    
'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
'''