class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0 
        maxCount = 0
        n = len(s)
        window = s[:k]
        for j in window: 
            if j in vowels: 
                count += 1
        maxCount = count
        for i in range(k, n): 
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels: 
                count -= 1
            maxCount = max(maxCount, count)

        return maxCount
            

        