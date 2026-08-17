class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product=nums[0]
        min_product=nums[0]
        answer=nums[0]

        for i in range(1,len(nums)):
            prev_max=max_product
            prev_min=min_product
            max_product = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            min_product = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            answer = max(answer, max_product)
        return  answer
    
