class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
            return head

        new_head = head.next
        current = head
        previous = None

        while current and current.next:
            first = current
            second = current.next
            third = second.next

            second.next = first
            first.next = third

            if previous:
                previous.next = second

            previous = first
            current = third

        return new_head
