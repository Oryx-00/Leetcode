class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        hash_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        index = len(s) - 1
        while index >= 0:
            if index >= 1 and hash_map[s[index]] > hash_map[s[index-1]]:
                result += hash_map[s[index]] - hash_map[s[index - 1]]
                index -= 2
            else:
                result += hash_map[s[index]]
                index -= 1
        return result




        