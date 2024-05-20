class Node:
    def __init__(self, distance, result):
        self.distance = distance
        self.result = result
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"d: {current_node.distance}, result: {current_node.result}", end="  ->  ")
            current_node = current_node.next
        print("None")

    def append(self, distance, result):
        new_node = Node(distance, result)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        # Orta noktayı bul
        mid = self.find_mid(head)
        mid_next = mid.next
        mid.next = None

        # Sol ve sağ yarılarda tekrar merge sort uygula
        left = self.merge_sort(head)
        right = self.merge_sort(mid_next)

        # Birleştirme işlemi
        return self.merge(left, right)

    def find_mid(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.distance < right.distance:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result