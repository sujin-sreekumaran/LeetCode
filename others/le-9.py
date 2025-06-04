# Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x) -> bool:
        if x < 0:
          return False
        x_copy = x
        reverse = 0

        while x > 0: 
            remove = x % 10
            reverse = (10*reverse) + remove
            x //= 10
        

        return reverse == x_copy
        

result = isPalindrome(121)
print(result)  # True        