#' % Data Structures
#' % Xu Tian
#' % 2017/03/22

#' # 155. Min Stack
class MinStack(object):
# 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        curMin = min(x, curMin) if curMin is not None else x  # curMin can be None or 0
        self.q.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q[-1][1]
        else:
            return None
