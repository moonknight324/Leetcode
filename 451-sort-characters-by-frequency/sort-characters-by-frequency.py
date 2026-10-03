class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True) # lambda is nameless fn sorting on values instead of chars. Reverse means in descending order 
        parts = []
        for key,val in freq:
            parts.append(key * val)
        
        return "".join(parts)