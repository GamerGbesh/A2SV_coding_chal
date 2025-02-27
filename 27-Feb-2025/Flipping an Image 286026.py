# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = [img[::-1] for img in image]
        for i, _ in enumerate(flipped):
            flipped[i] = [int(not x) for x in flipped[i]]
        return flipped