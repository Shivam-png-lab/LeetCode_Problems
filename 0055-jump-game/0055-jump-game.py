class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxstep=0
       

        for i in range(len(nums)):
            if i > maxstep:
                return False
            maxstep = max(maxstep, i+nums[i])
            if maxstep >=len(nums)-1:
                return True
