import heapq
class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0  # 用于处理优先级相同的情况

    def enqueue(self, item, priority):
        """
        将一个元素添加到优先队列中。
        :param item: 要添加的元素
        :param priority: 元素的优先级，数值越小优先级越高
        """
        # 因为heapq是最小堆，所以我们存储负优先级来实现最大堆的行为
        heapq.heappush(self._heap, (-priority, self._counter, item))
        self._counter += 1

    def dequeue(self):
        """
        从优先队列中移除并返回优先级最高的元素。
        :return: 优先队列中优先级最高的元素
        """
        if self.is_empty():
            raise IndexError("dequeue from an empty priority queue")
        # heapq.heappop 返回的是 (-priority, counter, item) 元组
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        """
        查看优先队列中优先级最高的元素但不移除它。
        :return: 优先队列中优先级最高的元素
        """
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        """
        检查优先队列是否为空。
        :return: 如果队列为空返回True，否则返回False
        """
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)
