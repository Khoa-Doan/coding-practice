# Time: O(n^2)
# Space: O(1)

class Insertion:
    
    # For each element, compare it with previous elements
    # Shift elements bigger than it to the right one time
    # Place the element to the correct position
    def sort(self, nums):
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1
            while i >= 0 and nums[i] > key:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = key

nums = [5,4,3,2,1]
sorting = Insertion()
sorting.sort(nums)
print(nums)