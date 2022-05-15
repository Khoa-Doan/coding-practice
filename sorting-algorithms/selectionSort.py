# Time: O(n^2)
# Space: O(1)

class Selection:
    
    # Find the smallest element in the array and swap it with the first element.
    # Find the second smallest element and swap with with the second element in the array.
    # Etc
    def sort(self, nums):
        for i in range(0, len(nums)):
            minI = i
            for j in range(i+1, len(nums)):
                if nums[minI] > nums[j]:
                    minI = j
            nums[minI], nums[i] = nums[i], nums[minI]

nums = [5,4,3,2,1]
sorting = Selection()
sorting.sort(nums)
print(nums)