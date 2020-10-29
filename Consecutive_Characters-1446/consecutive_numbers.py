class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        max  =  0
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                count += 1
                
            if s[i] != s[i+1]:
                count = 1
            if max < count:
                max = count
        if max == 0:
            return 1
        return max
