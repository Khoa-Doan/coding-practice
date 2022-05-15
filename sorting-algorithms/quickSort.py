# Time: average O(nlogn) worst O(n^2)
# Space: average O(logn) worst O(n) (recursive stack)

class Quick:
    
    # Takes last element as pivot
    # Places the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot
    def sort(self, nums):
        
        def partition(l, r):
            i = l
            pivot = nums[r] # choose last element as pivot
            
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i] # place the pivot at the correct position
            return i

        def quickSort(l, r):
            if l >= r:
                return
            
            pivotI = partition(l, r)
            quickSort(l, pivotI-1)
            quickSort(pivotI+1, r)

        quickSort(0, len(nums)-1)

nums = [5,4,3,2,1]
sorting = Quick()
sorting.sort(nums)
print(nums)