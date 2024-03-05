#Question 1

class CircularQueueArray:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):  
            print("enqueue None")
            return
        else:
            if(self.head == -1):  
                self.head = 0
            self.tail = (self.tail + 1) % self.k  
            self.queue[self.tail] = data
            print(f"enqueue {data}")

    def dequeue(self):
        if (self.head == -1):  
            print("dequeue None")
            return
        else:
            data = self.queue[self.head]
            if (self.head == self.tail):  
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
            print(f"dequeue {data}")
            return data

    def peek(self):
        if (self.head == -1):  
            print("peek None")
            return
        else:
            print(f"peek {self.queue[self.head]}")
            return self.queue[self.head]
        
#Question 2
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
            self.rear.next = self.front
        else:
            self.rear.next = temp
            self.rear = temp
            self.rear.next = self.front
        print(f"enqueue {data}")

    def dequeue(self):
        if self.front is None:
            print("dequeue None")
            return
        temp = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        print(f"dequeue {temp.data}")
        return temp.data

    def peek(self):
        if self.front is None:
            print("peek None")
            return
        print(f"peek {self.front.data}")
        return self.front.data
    
#Question 3
    
queue = CircularQueueArray(5)

queue.enqueue(1)  # enqueue 1
queue.enqueue(2)  # enqueue 2
queue.enqueue(3)  # enqueue 3
queue.enqueue(4)  # enqueue 4
queue.enqueue(5)  # enqueue 5
queue.enqueue(6)  # enqueue None
queue.dequeue()  # dequeue 1
queue.peek()  # peek 2
queue.dequeue()  # dequeue 2
queue.dequeue()  # dequeue 3
queue.dequeue()  # dequeue 4
queue.dequeue()  # dequeue 5
queue.dequeue()  # dequeue None
queue.peek()  # peek None
queue.enqueue(7)  # enqueue 7
queue.enqueue(8)  # enqueue 8
queue.enqueue(9)  # enqueue 9
queue.enqueue(10)  # enqueue 10
queue.enqueue(11)  # enqueue 11
queue.enqueue(12)  # enqueue None
queue.dequeue()  # dequeue 7
queue.peek()  # peek 8
queue.dequeue()  # dequeue 8
queue.dequeue()  # dequeue 9
queue.dequeue()  # dequeue 10
queue.dequeue()  # dequeue 11
queue.dequeue()  # dequeue None
queue.peek()  # peek None
queue.enqueue(13)  # enqueue 13
queue.enqueue(14)  # enqueue 14
queue.enqueue(15)  # enqueue 15
queue.enqueue(16)  # enqueue 16
queue.enqueue(17)  # enqueue 17
queue.enqueue(18)  # enqueue None
queue.dequeue()  # dequeue 13
queue.peek()  # peek 14
queue.dequeue()  # dequeue 14
queue.dequeue()  # dequeue 15
queue.dequeue()  # dequeue 16
queue.dequeue()  # dequeue 17
queue.dequeue()  # dequeue None
queue.peek()  # peek None