class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            currentsum = max(currentsum+nums[i], nums[i])
            if currentsum>maxsum:
                maxsum=currentsum
        return maxsum