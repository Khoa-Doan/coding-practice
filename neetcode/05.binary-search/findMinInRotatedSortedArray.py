class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            m = l + (r - l) // 2
            
            if m + 1 < len(nums) and nums[m] > nums[m+1]:
                return nums[m+1]
            elif m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            elif nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1