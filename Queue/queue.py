class Queue():

    class Node():
        def __init__(self, down, data, up):
            self.down = down
            self.data = data
            self.up = up
    
    def __init__(self):
        # self.down = down
        # self.data = data
        # self.up = up

        # pointers
        self.back = None
        self.front = None

    def _front(self, node: Node):
        if node.up == None:
            self.front = node
        else:
            raise(NotImplementedError)

    
    def _back(self, node: Node):
        if node.down == None:
            self.back = node
        else:
            raise(NotImplementedError)
            

    
    # def _front(self, node: Node):
    #     if node.up == None:
    #         self.front = node


    def _enqueue(self, data, node: Node):

        if node == None:
            node = self.Node(None, data, None)
            self._front(node)
        else:
            node = self.Node(None, data, node.down)

        self._back(node)
        
        return node

    def enqueue(self, data):

        self.back = self._enqueue(data, self.back)

        return self.back



if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    print(queue.back.data)
    print(queue.front.data)

