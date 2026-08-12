class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0]*len(nums)
        leftproduct = 1
        rightproduct = 1

        for i in range(len(nums)):
            result[i]=leftproduct
            leftproduct=leftproduct*nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]=rightproduct*result[i]
            rightproduct=rightproduct*nums[i]

        return result