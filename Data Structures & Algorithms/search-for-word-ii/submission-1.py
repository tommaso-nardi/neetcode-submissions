class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w
        ris = set()
        rows = len(board)
        cols = len(board[0])


        def ricorsione(x,y,nodo):
            lettera=board[x][y]
            cur=nodo.children[lettera]
            if cur.word:
                ris.add(cur.word)
                cur.word=False
            board[x][y]='#'
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                # Se la prossima lettera è nel Trie, allora continuiamo a scendere, visto che non rompe gli if
                if 0 <= dx < rows and 0 <= dy < cols:
                    prossima_lettera = board[dx][dy]
                    if prossima_lettera in cur.children:
                        ricorsione(dx, dy, cur)
            board[x][y]=lettera
            

        for x in range(rows):
            for y in range(cols):
                if board[x][y] in root.children:
                    ricorsione(x,y,root)

        return list(ris)
                        