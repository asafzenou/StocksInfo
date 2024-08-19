# import threading
# import time
#
# # יצירת אובייקט סמפור עם מספר מקסימלי של 2
# semaphore = threading.Semaphore(2)
#
# def worker(num):
#     print(f"Worker {num} waiting for semaphore")
#     with semaphore:
#         print(f"Worker {num} acquired semaphore")
#         time.sleep(2)
#         print(f"Worker {num} releasing semaphore")
#
# # יצירת שרשורים
# threads = []
# for i in range(4):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()
#
# # המתנה לסיום השרשורים
# for thread in threads:
#     thread.join()
#
# print("All workers are done!")
import heapq


# from queue import PriorityQueue
# Q = PriorityQueue()
# Q.put(2)
# Q.put(1)
# print("size= " + str(Q.qsize()))
# print("item= " + str(Q.get()))
# print("item= " + str(Q.get()))

# import heapq
# def find_k_largest_elements(arr, k):
#     if k == 0:
#         return []
#
#     # הפיכת הסימנים והמרה ל-Min Heap
#     max_heap = [-elem for elem in arr]
#     heapq.heapify(max_heap)
#
#     # הוצאה של k האיברים הגדולים ביותר
#     k_largest_elements = [-heapq.heappop(max_heap) for _ in range(k)]
#     print(max_heap)
#     return k_largest_elements
#
# # דוגמת שימוש
# arr = [10, 1, 5, 7, 2, 6]
# k = 3
# k_largest_elements = find_k_largest_elements(arr, k)
# print(f"{k} largest elements:", k_largest_elements)

# def reverse_string(s):
#     # המרת המחרוזת לרשימה כדי שנוכל לשנות את התווים במקום
#     s = list(s)
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         # חילוף התווים במצביעים השמאלי והימני
#         s[left], s[right] = s[right], s[left]
#         # התקדמות המצביעים
#         left += 1
#         right -= 1
#
#     # החזרת המחרוזת שהופכת חזרה לפורמט מחרוזת
#     return ''.join(s)
#
#
# # דוגמת שימוש
# original_string = "Intel"
# reversed_string = reverse_string(original_string)
# print(f"Original: {original_string}")
# print(f"Reversed: {reversed_string}")

# class Solution():
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heap = nums[:k]
#         print(heap)
#         heapq.heapify(heap)
#         print(heap)
#
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heappop(heap)  # O(1)
#                 heapq.heappush(heap, num)
#
#         return heap[0]
# solution = Solution()
# solution.findKthLargest([6,2,5,3,7,8,9,10], 5)

# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
#
#
# class Solution:
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         oldToCopy = {None: None}
#
#         cur = head
#         while cur:
#             copy = Node(cur.val)
#             oldToCopy[cur] = copy
#             cur = cur.next
#
#         cur = head
#         while cur:
#             copy = oldToCopy[cur]
#             copy.next = oldToCopy[cur.next]
#             copy.random = oldToCopy[cur.random]
#             cur = cur.next
#
#         return oldToCopy[head]
#
# def create_test_linked_list():
#     # Create nodes
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#
#     # Set up next pointers
#     node1.next = node2
#     node2.next = node3
#
#     # Set up random pointers
#     node1.random = node3
#     node2.random = node1
#     node3.random = node2
#
#     return node1
#
#
# solution = Solution()
# solution.copyRandomList(create_test_linked_list())


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# # דוגמה לשימוש
# print(gcd(12, 8))  # Output: 4

#
# class Solution():
#     def simplifyPath(self, path):
#         """
#         :type path: str
#         :rtype: str
#         """
#         stack = []
#         parts = path.split("/")
#
#         for part in parts:
#             if part == "" or part == ".":
#                 continue
#             elif part == "..":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(part)
#
#         return "/" + "/".join(stack)
#
# s = Solution()
# print(s.simplifyPath("/home/"))


# arr = [0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
# print(arr[:24])

def turing_machine(S):
    n = len(S)
    if n % 4 != 0:
        return "Rejected"

    k = n // 4
    part1, part2, part3, part4 = S[:k], S[k:2 * k], S[2 * k:3 * k], S[3 * k:]

    set1 = {'a', 'b', 'c'}
    set2 = {'a\'', 'b\'', 'c\''}
    set3 = {'a"', 'b"', 'c"'}
    set4 = {'a"\'', 'b"\'', 'c"\'"'}

    def all_in_set(part, valid_set):
        for ch in part:
            if ch not in valid_set:
                return False
        return True

    state = 'q0'

    if state == 'q0':
        if all_in_set(part1, set1):
            state = 'q1'
        else:
            state = 'q_reject'

    if state == 'q1':
        if all_in_set(part2, set2):
            state = 'q2'
        else:
            state = 'q_reject'

    if state == 'q2':
        if all_in_set(part3, set3):
            state = 'q3'
        else:
            state = 'q_reject'

    if state == 'q3':
        if all_in_set(part4, set4):
            state = 'q_accept'
        else:
            state = 'q_reject'

    if state == 'q_accept':
        return "Accepted"
    else:
        return "Rejected"


# דוגמה לבדיקה
S = "abca"
print(turing_machine(S))  # מדפיס "Accepted" או "Rejected" בהתאם לקלט




