class Solution:
    def countAndSay(self, n: int) -> str:
      #table = {}
      #table['1'] = '11'
      #table['2'] = '12'
      #table['3'] = '13'
      #table['11'] = '21'
      #table['111
      s = '1'
      ns = ''
      for i in range(2, n+1):
        l = len(s)
        j = 0
        
        while j < l:
          if (l-j)>=3 and s[j] == s[j+1] and s[j+1] == s[j+2]:
            ns += '3' + str(s[j])
            j += 3
          elif (l-j)>=2 and s[j] == s[j+1]:
            ns += '2' + str(s[j])
            j += 2
          elif (l-j)>=1:
            ns += '1' + str(s[j])
            j += 1

        s = ns
        ns = ''
        
      return s
        
        
