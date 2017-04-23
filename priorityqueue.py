import heapq


class PriorityQueueNode(object):
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue(object):
    def __init__(self):
        self.heap = []

    def insert(self, priority, value):
        heapq.heappush(self.heap, PriorityQueueNode(priority, value))

    def pop(self):
        return heapq.heappop(self.heap).value

    def __bool__(self):
        return bool(self.heap)
