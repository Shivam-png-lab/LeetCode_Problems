class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original=n
        sum=0
        product=1
        while n>0:
            digit=n%10
            sum+=digit
            product*=digit
            n=n//10
        if original%(sum+product)==0:
            return True
        else:
            return False
        
