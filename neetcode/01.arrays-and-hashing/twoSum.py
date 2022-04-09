class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        # Brute force
        # O(n^2)
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """   
        
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap:
                return [i, hashMap[n]]
            hashMap[target - n] = i