class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])

        def riempir(i):
            for x in range(cols):
                if matrix[i][x] != 0:
                    matrix[i][x] = 'T'

        def riempic(j):
            for x in range(rows):
                if matrix[x][j] != 0:
                    matrix[x][j] = 'T'

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    riempir(i)
                    riempic(j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'T':
                    matrix[i][j] = 0
