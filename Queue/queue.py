class Queue():

    class Node():
        def __init__(self, down, data, up):
            self.down = down
            self.data = data
            self.up = up
    
    def __init__(self):
        
        # pointers
        self.back = None
        self.front = None
        self.display = []

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
            

    def _enqueue(self, data, node: Node):

        if node == None or node.data == None:
            node = self.Node(None, data, None)
            self._front(node)
        else:
            node = self.Node(None, data, node)
            node.up.down = node

        self._back(node)
        
        return node

    def enqueue(self, data):

        self.back = self._enqueue(data, self.back)
        return self.back
    
    def dequeue(self):

        if self.front.data == None:
            raise Exception("front value in your queue is None")

        result = self.front.data
        
        self.front.data = None

        if self.front.down != None:
            
            self.front.down.up = None
            self._front(self.front.down)
            #self.front.down = None

        return result

    def peek(self):

        return self.front.data

    
    def _displayQueue(self, node):

        if node.down == None:
            if node.data != None:
                self.display.append(node.data)
            return

        
        self.display.append(node.data)
        self._displayQueue(node.down)
        
        
    def displayQueue(self):
        self._displayQueue(self.front)
        result = self.display

        self.display = []
        return result



if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)


    print(queue.peek())
    print(queue.displayQueue())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    queue.enqueue(500)

    print(queue.displayQueue())

    print(queue.peek())
    print(queue.back.data)

