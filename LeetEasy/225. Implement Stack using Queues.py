class MyStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        return None

        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.stack)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()