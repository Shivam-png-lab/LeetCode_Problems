class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>0:
            result=pow(x,n)    
        else:
            result=pow(1/x,-n)
        return result