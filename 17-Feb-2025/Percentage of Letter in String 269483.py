# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for item in s:
            if item == letter:
                count += 1
        return math.floor((count/len(s)) * 100)