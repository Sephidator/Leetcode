class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.head = Node(0, 0)
        self.tail = Node(233, 233)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.record_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            result = self.record_node[key]
            if self.length > 1 and result != self.head:
                result.pre.next = result.next
                result.next.pre = result.pre
                result.next = self.head.next
                result.pre = self.head
                result.pre = self.head
                result.next = self.head.next
                result.pre.next = result
                result.next.pre = result
            return result.value
        except KeyError:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            result = self.record_node[key]
            result.pre.next = result.next
            result.next.pre = result.pre
            self.length -= 1
            self.capacity += 1
        except KeyError:
            if self.capacity == 0:
                self.record_node.pop(self.tail.pre.key)
                self.tail.pre = self.tail.pre.pre
                self.tail.pre.next = self.tail
                self.capacity += 1
                self.length -= 1

        result = Node(key, value)
        result.next = self.head.next
        result.pre = self.head
        result.next.pre = result
        result.pre.next = result
        self.record_node[key] = result
        self.length += 1
        self.capacity -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
