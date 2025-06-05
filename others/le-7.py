# Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        n = abs(x)

        while n != 0: 
            remove = n % 10
            reverse = (10*reverse) + remove
            n //= 10
        
        if reverse > 2**31 - 1:
            return 0
        return -reverse if x < 0 else reverse    

        
        