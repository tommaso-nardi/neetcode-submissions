class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sx=0
        dx=len(matrix[0])-1
        for i in matrix:
            if i[sx] <= target:
                if i[dx] >= target:
                    for j in range(len(i)):
                        if i[j] == target:
                            return True
                    return False
        return False