class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == '(':
                stk.append(')')
            elif i == '{':
                stk.append('}')
            elif i == '[':
                stk.append(']')
            elif len(stk) == 0 or stk.pop() != i:
                return False
        return len(stk) == 0
        
            