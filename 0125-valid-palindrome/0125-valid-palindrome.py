class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        org = s
        res = ""

        for i in s:
            if i.isalnum():
                res += i
        
        left = 0
        right = len(res) - 1

        while left < right:
            if res[left] != res[right]:
                return False
                break
            left += 1
            right -= 1
        else:
            return True