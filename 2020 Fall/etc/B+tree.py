class Node(object):

   def __init__(self, order):
       self.order = order
       self.keys = []
       self.values = []
       self.leaf = True

   def insert_in_leaf(self, key, value):
       # Adds a key-value pair to the node.
       if not self.keys:
           self.keys.append(key)
           self.values.append([value])
           return None

       for i, item in enumerate(self.keys):
           if key == item:
               self.values[i].append(value)
               break

           elif key < item:
               self.keys = self.keys[:i] + [key] + self.keys[i:]
               self.values = self.values[:i] + [[value]] + self.values[i:]
               break

           elif i + 1 == len(self.keys):
               self.keys.append(key)
               self.values.append([value])
               break

   def split(self):
       # Splits the node into two and stores them as child nodes.
       left = Node(self.order)
       right = Node(self.order)
       mid = self.order / 2

       left.keys = self.keys[:mid]
       left.values = self.values[:mid]

       right.keys = self.keys[mid:]
       right.values = self.values[mid:]

       self.keys = [right.keys[0]]
       self.values = [left, right]
       self.leaf = False

   def is_full(self):
       # Returns True if the node is full.
       return len(self.keys) == self.order

   def show(self, counter=0):
       # Prints the keys at each level.
       print 'level', counter, str(self.keys)

       if not self.leaf:
           for item in self.values:
               item.show(counter+1)


class BPlusTree(object):
   '''
   B+ tree object, consisting of nodes.
   Nodes will automatically be split into two once it is full. When a split
   occurs, a key will 'float' upwards and be inserted into the parent node to
   act as a pivot.
   Attributes:
       order (int): The maximum number of keys each node can hold.
   '''
   def __init__(self, order=8):
       self.root = Node(order)

   def _find(self, node, key):
       '''
       For a given node and key, returns the index where the key should be
       inserted and the list of values at that index.
       '''
       for i, item in enumerate(node.keys):
           if key < item:
               return node.values[i], i

       return node.values[i + 1], i + 1

   def _merge(self, parent, child, index):
       '''
       For a parent and child node, extract a pivot from the child to be
       inserted into the keys of the parent. Insert the values from the child
       into the values of the parent.
       '''
       parent.values.pop(index)
       pivot = child.keys[0]

       for i, item in enumerate(parent.keys):
           if pivot < item:
               parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
               parent.values = parent.values[:i] + child.values + parent.values[i:]
               break

           elif i + 1 == len(parent.keys):
               parent.keys += [pivot]
               parent.values += child.values
               break

   def insert(self, key, value):
       '''
       Inserts a key-value pair after traversing to a leaf node. If the leaf
       node is full, split the leaf node into two.
       key : Pointer P
       value : value K
       '''
       parent = None
       child = self.root

       while not child.leaf:
           parent = child
           child, index = self._find(child, key)

       child.insert_in_leaf(key, value)

       if child.is_full():
           child.split()

           if parent and not parent.is_full():
               self._merge(parent, child, index)

   def find(self, key):
       # Returns a value for a given key, and None if the key does not exist.
       child = self.root

       while not child.leaf:
           child, index = self._find(child, key)

       for i, item in enumerate(child.keys):
           if key == item:
               return child.values[i]

       return None

   def show(self):
       #Prints the keys at each level.
       self.root.show()

def test():
   bplustree = BPlusTree(order=4)
   print('\nInsert [ 3, 5, 21, 14, 8, 9, 33, 16, 11, 27, 32 ]')
   bplustree.insert(3, '3')
   bplustree.insert(5, '5')
   bplustree.insert(21, '21')
   bplustree.insert(14, '14')
   bplustree.insert(8, '8')
   bplustree.insert(9, '9')
   bplustree.insert(33, '33')
   bplustree.insert(16, '16')
   bplustree.insert(11, '11')
   bplustree.insert(27, '27')
   bplustree.insert(32, '32')
   bplustree.show()

if __name__ == '__main__':

   print('\n--------------TEST---------------')
   test()

