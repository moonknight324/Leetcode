class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        rotated = s
        left = ''
        if len(s) == 0:
            return False
        i = 0
        while(i < len(s)):
            left = rotated[0]
            rotated = rotated[1:] + left
            if rotated == goal:
                return True
            i += 1
        return False