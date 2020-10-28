class Solution(object):
    def bitwiseComplement(self, N):
        
        """
        :type N: int
        :rtype: int
        """
        from math import log
        if N == 0:
             return 1
        print('Complement of Base 10 Integer'.replace(' ','_').lower())
        return pow(2, int(log(N, 2))+1) - N - 1

