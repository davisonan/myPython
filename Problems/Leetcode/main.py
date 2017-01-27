# 461. Hamming Distance
# nTrials: 2
# Didn't notice that 0 digit doesn't count 
# when one number has more bits than the other

# Solution 1: The straightforward solution by comparing
# digits. Note the missing 0 digits should be filled.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x > 0 and y > 0:
            digit1 = x % 2
            digit2 = y % 2
            count += abs(digit1 - digit2)
            x //= 2
            y //= 2
        else:
            if x == 0:
                while y > 0:
                    count += y % 2
                    y //= 2
            else:
                while x > 0:
                    count += x % 2
                    x //= 2
        return count

sol = Solution()
sol.hammingDistance(1, 4)

# Solution 2: Found in the forum, neat and concise.
# Need to develop this type of tricky solution.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')  # x^y

sol = Solution()
sol.hammingDistance(1, 4)
