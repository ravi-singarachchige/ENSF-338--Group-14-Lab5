import timeit
import random

# Mergesort function for sorting the queue
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

# Priority Queue Class using Mergesort
class PriorityQueueMergesort:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        merge_sort(self.queue)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

# Priority Queue Class with Sorted Insertion
class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if not self.queue:
            self.queue.append(item)
        else:
            for i in range(len(self.queue)):
                if item < self.queue[i]:
                    self.queue.insert(i, item)
                    break
            else:
                self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

# Function to generate random tasks
def generate_tasks(num_tasks=1000, enqueue_prob=0.7):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < enqueue_prob:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue',))
    return tasks

# Function to test performance of priority queues
def test_performance(queue_class, task_lists):
    def run_queue_tasks(tasks):
        queue = queue_class()
        for task in tasks:
            if task[0] == 'enqueue':
                queue.enqueue(task[1])
            elif task[0] == 'dequeue':
                queue.dequeue()
                
    times = []
    for tasks in task_lists:
        start_time = timeit.default_timer()
        run_queue_tasks(tasks)
        times.append(timeit.default_timer() - start_time)
    
    return times

# Generate 100 random task lists
random.seed(42)  # Ensuring reproducibility
task_lists = [generate_tasks() for _ in range(100)]

# Measure performance for both implementations
mergesort_times = test_performance(PriorityQueueMergesort, task_lists)
sortedinsert_times = test_performance(PriorityQueueSortedInsert, task_lists)

# Calculate and print average times for comparison
average_mergesort_time = sum(mergesort_times) / len(mergesort_times)
average_sortedinsert_time = sum(sortedinsert_times) / len(sortedinsert_times)

print("Average time for PriorityQueueMergesort:", average_mergesort_time)
print("Average time for PriorityQueueSortedInsert:", average_sortedinsert_time)

#Question 5 
#The sorted insertion priority queue is faster because it minimizes overhead by inserting elements in their correct position, avoiding the need for full array sorts after each insertion. In contrast, the mergesort-based queue requires sorting the entire array after each enqueue, leading to higher computational costs as the queue grows.