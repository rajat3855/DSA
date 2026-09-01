class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oneStep = head
        twoStep = head

        while twoStep and twoStep.next:
            oneStep = oneStep.next
            twoStep = twoStep.next.next

        return oneStep
