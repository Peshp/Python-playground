class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        num = 0
        curWord = "";
        
        for i in range(len(strs) - 1):
            curWord = strs[i]
            nextWord = strs[i + 1]
            smaller = min(curWord, nextWord)
            length = len(smaller) - 3
            for j in range(len(smaller)):
                if j > length:
                    break
                current = curWord[j]
                next_letter = nextWord[j]
                if current == next_letter:
                    prefix += current
        return prefix
    
sol = Solution()
output = sol.longestCommonPrefix(["flow","flight","car"])
print(output)
            