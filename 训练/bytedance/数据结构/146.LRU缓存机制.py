# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.pre = None
#         self.next = None
#
#
# class LRUCache(object):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.length = 0
#         self.head = Node(0, 0)
#         self.tail = Node(233, 233)
#         self.head.next = self.tail
#         self.tail.pre = self.head
#         self.record_node = {}
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         try:
#             result = self.record_node[key]
#             # 对于拿到的某个result
#             # 1. 从链表中删除该节点
#             # 2. 把这个result插入到头节点的下一个
#             # 3. 修改头节点的next和原来"头节点next的pre"这两个指针
#             if self.length > 1 and result != self.head:
#                 result.pre.next = result.next
#                 result.next.pre = result.pre
#                 result.pre = self.head
#                 result.next = self.head.next
#                 result.pre.next = result
#                 result.next.pre = result
#             return result.value
#         except KeyError:
#             return -1
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         # PUT的时候，
#         # 如果这个key对应的节点存在的话，
#         # 删除这个节点
#         # 如果这个节点不存在的话，不做这一步操作
#         # 但是如果capacity为0的话，就要删掉尾部的一个节点来空出位子
#         try:
#             result = self.record_node[key]
#             result.pre.next = result.next
#             result.next.pre = result.pre
#             self.length -= 1
#             self.capacity += 1
#         except KeyError:
#             if self.capacity == 0:
#                 self.record_node.pop(self.tail.pre.key)
#                 self.tail.pre = self.tail.pre.pre
#                 self.tail.pre.next = self.tail
#                 self.capacity += 1
#                 self.length -= 1
#
#         # 并在head处添加对应key的新节点
#         # 在字典中注册这个node
#         # 修改capacity信息
#         result = Node(key, value)
#         result.next = self.head.next
#         result.pre = self.head
#         result.next.pre = result
#         result.pre.next = result
#         self.record_node[key] = result
#         self.length += 1
#         self.capacity -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.records = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        try:
            result = self.records[key]
            result.pre.next = result.next
            result.next.pre = result.pre
            result.pre = self.head
            result.next = self.head.next
            result.pre.next = result
            result.next.pre = result
            return result.value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            record = self.records[key]
            record.pre.next = record.next
            record.next.pre = record.pre
            self.capacity += 1
        except KeyError:
            if self.capacity is 0:
                node_to_remove = self.tail.pre
                node_to_remove.pre.next = self.tail
                node_to_remove.next.pre = node_to_remove.pre
                self.records.pop(node_to_remove.key)
                self.capacity += 1

        new_record = Node(key, value)
        self.records[key] = new_record
        new_record.pre = self.head
        new_record.next = self.head.next
        new_record.pre.next = new_record
        new_record.next.pre = new_record
        self.capacity -= 1


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
