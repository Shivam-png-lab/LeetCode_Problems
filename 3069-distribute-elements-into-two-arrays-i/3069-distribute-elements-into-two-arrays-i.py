class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [nums[0]]
        arr1 = [nums[1]]

        for i in range(2, len(nums)):
            if arr[-1] > arr1[-1]:
                arr.append(nums[i])
            else:
                arr1.append(nums[i])

        return arr + arr1