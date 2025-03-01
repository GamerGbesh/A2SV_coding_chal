# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o: list[tuple[int, int]] = []
        y: list[tuple[int, int]] = []
        for i, list1 in enumerate(board):
            for j, number in enumerate(list1):
                count = 0
                # Same line

                if j != len(list1) - 1 and list1[j + 1] == 1:
                    count += 1
                if j != 0 and list1[j - 1] == 1 :
                    count += 1
                
                # Above
                if i != 0:
                    if board[i - 1][j] == 1:
                        count += 1
                    if j != len(list1) - 1 and board[i - 1][j + 1] == 1:
                        count += 1
                    if j != 0 and board[i - 1][j - 1] == 1:
                        count += 1
                # Below
                if i != len(board) - 1:
                    if board[i + 1][j] == 1:
                        count += 1
                    if j != len(list1) - 1 and board[i + 1][j + 1] == 1 :
                        count += 1
                    if j != 0 and board[i + 1][j - 1] == 1 :
                        count += 1
                
                if number == 1:
                    if count < 2:
                        o.append((i, j))
                    elif count > 3:
                        o.append((i, j))
                    
                else:
                    if count == 3:
                        y.append((i, j))
        for i, j in o:
            board[i][j] = 0
        for i, j in y:
            board[i][j] = 1