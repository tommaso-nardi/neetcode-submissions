class Solution:
    def validPalindrome(self, s: str) -> bool:
        indices = 0
        indiced = len(s)-1
        def backup(indices,indiced):
            while indices<indiced:
                if not s[indices].isalnum():
                    indices += 1
                    continue
                elif not s[indiced].isalnum():
                    indiced -= 1
                    continue
                if s[indices].lower()==s[indiced].lower():
                    indices=indices+1
                    indiced=indiced-1
                else:
                    return False
            return True
        
        while indices<indiced:
            if not s[indices].isalnum():
                indices += 1
                continue
            elif not s[indiced].isalnum():
                indiced -= 1
                continue
            if s[indices].lower()==s[indiced].lower():
                indices=indices+1
                indiced=indiced-1
            else:
                return backup(indices+1,indiced) or backup(indices,indiced-1)
        return True