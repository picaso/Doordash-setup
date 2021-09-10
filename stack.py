import unittest

class StackTest(unittest.TestCase):
    def test_should_find_length_of_a_stack(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        self.assertEqual(stack.length(), 0)
    
    def test_should_append_element_to_a_stack(self):
            stack = Stack()
            stack.push("hello")
            stack.push("world")
            self.assertEqual(len(stack), 2)
            self.assertEqual(stack.length(), 2)


class Stack():
    def __init__(self) -> None:
        # self.stack.append(element) to push
        # self.stack.pop() to remove 
        self.stack = []

    def __len__(self):
        return len(self.stack)
    
    def length(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)