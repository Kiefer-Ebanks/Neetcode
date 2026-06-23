class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        real_row = -1

        while top <= bot:
            m = (top + bot) // 2

            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                real_row = m
                break


        if not (top <= bot):
            return False


        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) //2

            if matrix[real_row][m] < target:
                l = m+1
            elif matrix[real_row][m] > target:
                r = m-1
            else:
                return True

        return False
            




        