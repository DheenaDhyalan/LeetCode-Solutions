class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x//10
        
        if org == rev:
            return True
        else:
            return False
