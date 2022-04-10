class Solution:
    def isHappy(self, n: int) -> bool:
        """
        if n == 0:
            return False
        
        Set = set()
        while n != 1:
            curSum = 0
            while n > 0:
                curSum += (n % 10)**2
                n = n // 10
            if curSum in Set:
                return False
            Set.add(curSum)
            n = curSum
        return True
        """
    
    # Using the same idea as linked list cycle
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)
        
        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False
            
    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output