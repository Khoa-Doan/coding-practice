class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Brute force
        """
        maxSum = float('-inf')
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                maxSum = max(maxSum, sum(nums[i:j+1]))
        return maxSum
        """
        
        # It is given that the array has at least one element
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum