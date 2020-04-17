class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        str_len = len(s)
        res = 0
        i = 0
        while i < str_len:
            next_two = s[i:i+2]
            if next_two in values.keys():
                res += values[next_two]
                i += 2
            else:
                res += values[s[i]]
                i += 1
                
        return res
