# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counts = {}
        for i, arr in enumerate(mat):
            sum_arr = sum(arr)
            if sum_arr not in counts:
                counts[sum_arr] = i
        max_num = max(counts.keys())
        return [counts[max_num], max_num]