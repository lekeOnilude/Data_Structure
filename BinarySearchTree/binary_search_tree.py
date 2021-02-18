# Builing a Binary Search Tree from Scrach


class Node():

    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree():

        
    def __init__(self):
        # write a code to check if the BST is valid
        self.root = None

        

    def _add(self, elem: int, node: Node):

        if node == None: # check if the tree is empty
            node = Node(None, None, elem)
            #tree.append(node.data)
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
        #node = self.find(elem, node)

        if self.find(elem, node) == None:
            return
        
        if elem > node.data:
            node = self.find(elem, node.right)
        elif elem < node.data:
            node = self.find(elem, node.left)
        else:

            if node.right == None and node.left == None:
                node.data = None
            elif node.right != None and node.left == None:
                node = node.right

                #node.right = None
                print(node.data)
            elif node.left != None and node.right == None:
                node = node.left
                node.left = None
            elif node.right != None and node.left != None:
                #node_Remove = node
                farleft = self.farleft(node)
                print(farleft.data+"#hhhh")
                node.data = farleft.data
                self.remove(farleft.data, node)
        
        return node



    
    def find(self, elem, node):
        
        if node.data == elem:
            return node

        if elem > node.data:
            node = self.find(elem, node.right)
        elif elem < node.data:
            node = self.find(elem, node.left)
        
        return node
        
        
    

    def farleft (self, node):
        if node == None:
            return
            
        node = self.farleft(node.left)

        return node
        
    

    def preorder (self, node):
        if node == None:
            #print(None)
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
    
    

    result = bst.find(2, node)
    print(result.data)

    #bst.preorder(node)

    #remove = bst.remove(30, node)

    #bst.preorder(remove)