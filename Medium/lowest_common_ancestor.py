
class Tree:

    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if not self.key:
            self.key = value
        if self.key < value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Tree(value)
                self.right.parent = self
                return self.right
        elif self.key > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Tree(value)
                self.left.parent = self
                return self.left

    def search(self, key):
        if self.key == key:
            return self
        if self.key < key:
            if self.right:
                return self.right.search(key)
            return False
        if self.key > key:
            if self.left:
                return self.left.search(key)
            return False

    def insert_list(self, items):
        for i in items:
            self.insert(i)

    def traverse(self):
        ordered = []
        if self.left:
            ordered += self.left.traverse()
        ordered.append(self.key)
        if self.right:
            ordered += self.right.traverse()
        return ordered

    def get_ancestors(self):
        ancestors = []
        temp = self.parent
        while temp is not None:
            ancestors += [temp.key]
            temp = temp.parent
        return ancestors

t = Tree()
t.insert_list([30,8,52,3,20,10,29])



