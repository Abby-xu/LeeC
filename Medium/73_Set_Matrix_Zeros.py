class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        tar_rows = []
        tar_cols = []
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    tar_rows.append(i)
                    tar_cols.append(j)
        print(tar_rows)
        for i in range(0, n):
            for j in range(0, m):
                if i in tar_rows or j in tar_cols:
                    matrix[i][j] = 0   
        
        