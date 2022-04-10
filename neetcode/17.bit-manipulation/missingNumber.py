class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Math way
        """
        ans = len(nums) #Initialize ans = n
        for i in range(len(nums)):
            ans = ans + i - nums[i]
        return ans
        """
    
        # Bit manipulation
        ans = len(nums) #Initialize ans = n
        for i in range(len(nums)):
            ans = ans ^ i ^ nums[i]
        return ans