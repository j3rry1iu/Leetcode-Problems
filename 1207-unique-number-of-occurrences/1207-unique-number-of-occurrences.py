class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        for i in arr: 
            count_dict[i] = count_dict.get(i, 0) + 1
        freq = count_dict.values()
        return len(freq) == len(set(freq))
        