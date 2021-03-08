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
        prev_element = 1000 # Greatest is 'M'
        while i < str_len:
            next_two = s[i:i+2]
            if next_two in values.keys():
                element = values[next_two]
                if element <= prev_element:
                    res += element
                    element = prev_element
                i += 2
            else:
                element = values[s[i]]
                if element <= prev_element:
                    res += element
                    element = prev_element
                i += 1
                
        return res
