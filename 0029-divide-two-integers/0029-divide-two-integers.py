class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count=0
        negative=False
        if dividend < 0:
            dividend = -dividend
            negative = not negative

        if divisor < 0:
            divisor = -divisor
            negative = not negative

        while dividend >= divisor:
            chunk = divisor
            multiple = 1

            while dividend >= chunk + chunk:
                chunk = chunk + chunk
                multiple = multiple + multiple

            dividend = dividend - chunk
            count = count + multiple

        if negative:
            count = -count

        if count > 2147483647:
            count = 2147483647

        if count < -2147483648:
            count = -2147483648

        return count