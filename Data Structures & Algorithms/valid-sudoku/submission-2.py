class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictlinee=defaultdict(set)
        dictcolonne=defaultdict(set)
        dictquadri=defaultdict(set)
        for i in range(9):
            for j in range(9):
                numero = board[i][j]
                if numero ==".":
                    continue
                if numero in dictlinee[i] or numero in dictcolonne[j] or numero in dictquadri[(i//3)*3+(j//3)]:
                    return False
                dictlinee[i].add(numero)
                dictcolonne[j].add(numero)
                dictquadri[(i//3)*3+(j//3)].add(numero)
        return True