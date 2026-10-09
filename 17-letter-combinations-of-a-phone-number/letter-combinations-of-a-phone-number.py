class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []

        def backtrackfn(combination,ndigits):
            if len(ndigits) == 0:
                result.append(combination)
                return 
            else:
                for letter in phone[ndigits[0]]:
                    backtrackfn(combination + letter, ndigits[1:])

        if digits:
            backtrackfn('',digits)
        return result
        