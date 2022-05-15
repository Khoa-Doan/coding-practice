# Time: O(nlogn)
# Space: O(n) (longest sortedArr array has length n)

import rlcompleter


class Merge:
    
    # Divide and conquer is each of the array, then merge them together
    def sort(self, nums):
        
        def merge(l, r):
            if l == r:
                return

            m = (l + r) // 2
            merge(l, m)
            merge(m+1, r)

            i, j = l, m+1
            sortedArr = []
            while i <= m or j <= r:
                leftVal = nums[i] if i <= m else float('inf')
                rightVal = nums[j] if j <= r else float('inf')
                if leftVal < rightVal:
                    sortedArr.append(nums[i])
                    i += 1
                else:
                    sortedArr.append(nums[j])
                    j += 1
            for k in range(len(sortedArr)):
                nums[l+k] = sortedArr[k]

        merge(0, len(nums)-1)

nums = [5,4,3,2,1]
sorting = Merge()
sorting.sort(nums)
print(nums)