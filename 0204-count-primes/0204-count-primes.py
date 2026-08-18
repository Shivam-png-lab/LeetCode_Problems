class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        if n <= 2:
            return 0

        is_prime = bytearray(b'\x01') * n
        is_prime[0:2] = b'\x00\x00'

        p = 2

        while p * p < n:
            if is_prime[p]:
                count = (n - 1 - p * p) // p + 1
                is_prime[p * p:n:p] = b'\x00' * count
            p += 1

        return sum(is_prime)   