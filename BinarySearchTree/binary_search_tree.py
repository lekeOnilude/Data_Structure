# Builing a Binary Search Tree from Scrach

import pdb

class Node():

    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree():

        
    def __init__(self):
        self.root = None

        

    def _add(self, elem: int, node: Node):

        if node == None: # check if the tree is empty
            node = Node(None, None, elem)

        else:
            
            if elem > node.data:
                node.right = self._add(elem, node.right)
            else:
                node.left = self._add(elem, node.left)

        return node

    
    def add (self, elem):
        self.root = self._add(elem, self.root)

        return self.root


    def remove(self, elem, node):

        if node == None:
            return None
        
        if elem > node.data:
            node.right = self.remove(elem, node.right)
        elif elem < node.data:
            node.left = self.remove(elem, node.left)
        else:

            if node.left == None:
                rightChild = node.right

                node.data = None
                node = None

                return rightChild
            elif node.right == None:

                leftChild = node.left
                node.data = None
                node = None
                return leftChild
            elif node.right != None and node.left != None:
                
                farleft = self.findMin(node).data
                leftChild = self.remove(farleft, node)
                node.data = farleft

                return leftChild
        
        return node



    
    def find(self, elem, node):
        
        if node.data == elem:
            return node

        if elem > node.data:
            node = self.find(elem, node.right)
        elif elem < node.data:
            node = self.find(elem, node.left)
        
        return node

           
    
    # search far left as far as possible
    def findMin (self, node):
        if node.left == None:
            return node
        else:
            lowestValue = self.findMin(node.left)

        return lowestValue
        
    

    def preorder (self, node):
        if node == None:
            return
        
        print(node.data)

        self.preorder(node.left)
        self.preorder(node.right)


        


if __name__ == "__main__":
    bst = BinarySearchTree()
    
    node = bst.add(20)
    bst.add(30)
    bst.add(40)
    bst.add(2)
    bst.add(70)
    bst.add(10)
    bst.add(35)
    bst.add(1)

    
    #print(bst.findMin(node).data)
    remove = bst.remove(20, node)
    bst.preorder(node)