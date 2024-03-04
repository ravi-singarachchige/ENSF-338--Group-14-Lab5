import timeit
import random
import matplotlib.pyplot as plt

# Question 1
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Question 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.head
        self.head = self.head.next
        return popped.data

    def is_empty(self):
        return self.head is None

# Question 3
def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        task = "push" if random.random() < 0.7 else "pop"
        tasks.append(task)
    return tasks

# Question 4
def measure_performance(stack_class, tasks):
    stack = stack_class()
    start_time = timeit.default_timer()
    for task in tasks:
        if task == "push":
            stack.push(1)  
        elif task == "pop":
            stack.pop()
    end_time = timeit.default_timer()
    return end_time - start_time

# Question 5
def plot_distribution(times1, times2):
    plt.hist(times1, bins=20, alpha=0.5, label='ArrayStack')
    plt.hist(times2, bins=20, alpha=0.5, label='LinkedListStack')
    plt.legend(loc='upper right')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency')
    plt.title('Performance Distribution')
    plt.show()

if __name__ == "__main__":
    # Generate tasks
    tasks = [generate_random_tasks() for _ in range(100)]

    # Measure performance
    times_array = [measure_performance(ArrayStack, task) for task in tasks]
    times_linked = [measure_performance(LinkedListStack, task) for task in tasks]

    # Print results
    print("ArrayStack Performance:", times_array)
    print("LinkedListStack Performance:", times_linked)

    # Plot distribution
    plot_distribution(times_array, times_linked)
    
# Discussion for Question 5 :-
# The stack implementation using Arrays takes less time than the one using Linked list. 
# Therefore, it can be concluded that the stack implementation using Arrays has better performance than that with
# Linked list. 
