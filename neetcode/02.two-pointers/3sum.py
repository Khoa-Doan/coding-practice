class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, n in enumerate(nums):
            if i >= 1 and n == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = n + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ans.append([n, nums[left], nums[right]])
                    # avoid duplicates
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return ans