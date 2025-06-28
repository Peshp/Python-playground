class Solution(object):
    def isPalindrome(self, x):
        number = str(x)
        reversed = ""
        for char in number:
            reversed = char + reversed
        if reversed == number:
            return True
        return False    
    
sol = Solution()
result = sol.isPalindrome(17)
print(result)  


        