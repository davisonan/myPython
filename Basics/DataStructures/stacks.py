#' % Stack data structure
#' % Xu Tian
#' % 2017/04/10

#' # Background
#' last in first out

#' completely separate the implementations from the interfaces.

class aListStack(object):
    """This is a stack implemented with a list internally."""
    def __init__(self):
        self.vals = []

    def size(self):
        """Return the size of the stack."""
        return len(self.vals)

    def __len__(self):
        """Return the size of the stack."""
        return self.size()

    def isEmpty(self):
        """Return True if the stack is empty, otherwise, False."""
        return self.size() == 0

    def push(self, val):
        """Push a value into the stack."""
        self.vals.append(val)

    def pop(self):
        """Remove the last value and return it."""
        if not self.isEmpty():
            return self.vals.pop()
        else:
            raise ValueError("No value in the stack.")


class aLinkedListStack(object):
    """This is a stack implemented with a linked list internally."""

    class Node(object):
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        self. = []

    def size(self):
        """Return the size of the stack."""
        return len(self.vals)

    def __len__(self):
        """Return the size of the stack."""
        return self.size()

    def isEmpty(self):
        """Return True if the stack is empty, otherwise, False."""
        return self.size() == 0

    def push(self, val):
        """Push a value into the stack."""
        self.vals.append(val)

    def pop(self):
        """Remove the last value and return it."""
        if not self.isEmpty():
            return self.vals.pop()
        else:
            raise ValueError("No value in the stack.")
