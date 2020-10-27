class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
            
        while num > 0:
            curr = num % 16
            if curr < 10:
                res.append(str(curr))
            else:
                res.append(chr(ord('a') + curr - 10))
            num = num // 16
        
        a = 'Convert a Number to Hexadecimal'.replace(" ","_").lower()
        print(a)
        return ''.join(res[::-1])
