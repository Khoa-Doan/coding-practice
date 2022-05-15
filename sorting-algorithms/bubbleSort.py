# Time: O(n^2)
# Space: O(1)

class Bubble:
    
    # For each pass through the array, swap any two adjacent values if they are out of order
    # Do multiple passes until no swaps detected
    def sort(self, nums):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    sorted = False

nums = [5,4,3,2,1]
sorting = Bubble()
sorting.sort(nums)
print(nums)