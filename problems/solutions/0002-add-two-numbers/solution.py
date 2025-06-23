from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to start the result linked list
        dummy = ListNode()
        res = dummy  # This will be used to return the result

        total = carry = 0  # Initialize total and carry variables

        # Loop until both lists are fully traversed and there's no carry left
        while l1 or l2 or carry:
            total = carry  # Start with carry from the previous step

            if l1:
                total += l1.val  # Add l1's value if it exists
                l1 = l1.next     # Move to the next node in l1
            if l2:
                total += l2.val  # Add l2's value if it exists
                l2 = l2.next     # Move to the next node in l2
            
            # Compute the new digit and update the carry
            num = total % 10      # Digit to store in the node
            carry = total // 10   # Carry for the next step
            
            # Create a new node with the computed digit and link it
            dummy.next = ListNode(num)
            dummy = dummy.next    # Move dummy to the new node
        
        # Return the next node after the dummy, which is the actual head of the result list
        return res.next
