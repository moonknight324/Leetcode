class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return  ""
        result = ""
        base = strs[0]

        for i in range(0,len(base)):
            for word in strs[1:]:  # because base has 0th index already so compare with 1st index element
                if i == len(word) or word[i] != base[i]:
                    return result
            result += base[i]
        
        return result  # in case any string in arr is empty