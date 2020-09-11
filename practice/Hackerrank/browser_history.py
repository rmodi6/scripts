'''
Most frequently used first followed by most recently used -
Input:
www.bloomberg.com
www.bbc.com
www.amazon.com
www.bloomberg.com

Output:
www.bloomberg.com
www.amazon.com
www.bbc.com
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
    
    def add(self, url):
        curr_node = Node(url)
        if not self.head:
            self.head = curr_node
        else:
            self.head.next = curr_node
            curr_node.prev = self.head
            self.head = curr_node
        return curr_node
    
    def delete(self, node):
        if node.prev is None and node.next is None:
            self.head = None
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        del node
        
    def head(self):
        return self.head
    
    def peek(self):
        if not self.head:
            return self.head.val
        else:
            return None

class Manager:
    def __init__(self):
        self.hmap = {}
        self.stack = Stack()
        
def visited(self, url):
    if url in self.hmap and self.stack.peek() == url:
        return
    if url in self.hmap:
        self.stack.delete(self.hmap[url])
    node = self.stack.add(url)
    self.hmap[url] = node
    
    
def history(self):
    li = []
    head = self.stack.head()
    while head:
        li.append(head.val)
        head = head.next
    return li
