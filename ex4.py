#Question 1

class Queue:
    def __init__(self):
        self.queue = []

    # Insert method to add element
    def enqueue(self, val):
        self.queue.insert(0, val)

    # Pop method to remove element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

    # Display  the queue
    def display(self):
        return self.queue
    
#Question 2

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            new_node.next, self.head = self.head, new_node
        else:
            self.head = self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        return removed_data
    
#Question 3

import random

def generate_tasks():
    tasks = []
    for _ in range(10000):
        task = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task)
    return tasks

#Question 4

import timeit

# Initialize the queues
queue_array = Queue()
queue_linked_list = Queue()

# Generate the tasks
task_lists = [generate_tasks() for _ in range(100)]

# Measure the time for the array-based queue
start_time = timeit.default_timer()
for tasks in task_lists:
    for task in tasks:
        if task == 'enqueue':
            queue_array.enqueue(1)
        else:
            queue_array.dequeue()
array_time = timeit.default_timer() - start_time

# Measure the time for the linked list-based queue
start_time = timeit.default_timer()
for tasks in task_lists:
    for task in tasks:
        if task == 'enqueue':
            queue_linked_list.enqueue(1)
        else:
            queue_linked_list.dequeue()
linked_list_time = timeit.default_timer() - start_time

# Print the results
print(f"Array-based Queue: {array_time} seconds")
print(f"Linked List-based Queue: {linked_list_time} seconds")

#Question 5

import matplotlib.pyplot as plt
import seaborn as sns

# Initialize the queues
queue_array = Queue()
queue_linked_list = Queue()

# Generate the tasks
task_lists = [generate_tasks() for _ in range(100)]

# Lists to store the times
array_times = []
linked_list_times = []

# Measure the time for each implementation multiple times
for _ in range(100):
    start_time = timeit.default_timer()
    for tasks in task_lists:
        for task in tasks:
            if task == 'enqueue':
                queue_array.enqueue(1)
            else:
                queue_array.dequeue()
    array_times.append(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    for tasks in task_lists:
        for task in tasks:
            if task == 'enqueue':
                queue_linked_list.enqueue(1)
            else:
                queue_linked_list.dequeue()
    linked_list_times.append(timeit.default_timer() - start_time)

# Plot the distributions
sns.distplot(array_times, hist = False, kde = True, label='Array')
sns.distplot(linked_list_times, hist = False, kde = True, label='Linked List')
plt.legend(prop={'size': 12})
plt.title('Time Distribution')
plt.xlabel('Time (s)')
plt.ylabel('Density')
plt.show()

