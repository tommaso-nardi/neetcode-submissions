class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        tastierino = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ris=[]
        def ricorsione(i,stringaattuale):
            if i == len(digits):
                ris.append(stringaattuale)
                return

            numero=digits[i]
            lettere=tastierino[numero]

            for l in lettere:
                ricorsione(i+1,stringaattuale+l)

        ricorsione(0,"")
        return ris