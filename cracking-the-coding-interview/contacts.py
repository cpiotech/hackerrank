class TriesNode(object):
    __slots__ = ["char", "children", "is_word", "word_count"]

    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_word = False
        self.word_count = 0
    def get_child(self, c):
        for child in self.children:
            if child.char == c:
                return child
        return None

class Tries(object):
    def __init__(self):
        self.root = TriesNode('*')
    def add(self, word):
        curr = self.root
        for c in word:
            next_node = curr.get_child(c)
            if next_node is None:
                next_node = TriesNode(c)
                curr.children.append(next_node)
            next_node.word_count += 1
            curr = next_node
        curr.is_word = True
    def find(self, prefix):
        curr = self.root
        for c in prefix:
            next_node = curr.get_child(c)
            if next_node is None:
                return 0
            curr = next_node
        return curr.word_count

o = Tries()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        o.add(contact)
    elif op == 'find':
        print o.find(contact)
