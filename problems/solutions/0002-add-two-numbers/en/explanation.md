# 2. Add Two Numbers - Solution Explanation

## Approach: Linked List Addition Simulation

This solution simulates the process of adding two numbers represented as linked lists, where each node contains a digit and they are ordered from least significant digit to most significant digit (reverse order).

## Algorithm Logic:

1. We create a "dummy" node to start our result list, making it easier to return the final head.
2. We initialize variables for the total and carry.
3. We traverse both lists and continue as long as there are nodes in either list or there is a pending carry.
4. For each position:
   - We start with the value of the previous carry
   - We add the values of the current nodes (if they exist)
   - We calculate the new digit (remainder of division by 10) and new carry (quotient of division by 10)
   - We create a new node with the calculated digit and add it to the result list

## Step-by-Step Example:

Using the example: `l1 = [2,4,3]` and `l2 = [5,6,4]` representing 342 and 465 respectively.

1. Initialization:

   - `dummy = ListNode(0)`, `res = dummy`
   - `total = 0`, `carry = 0`

2. Iteration 1:

   - `total = 0` (initial carry)
   - `l1.val = 2`, `total = 2`, `l1` advances
   - `l2.val = 5`, `total = 7`, `l2` advances
   - `num = 7 % 10 = 7`, `carry = 7 // 10 = 0`
   - We add `ListNode(7)` to the result list

3. Iteration 2:

   - `total = 0` (previous carry)
   - `l1.val = 4`, `total = 4`, `l1` advances
   - `l2.val = 6`, `total = 10`, `l2` advances
   - `num = 10 % 10 = 0`, `carry = 10 // 10 = 1`
   - We add `ListNode(0)` to the result list

4. Iteration 3:

   - `total = 1` (previous carry)
   - `l1.val = 3`, `total = 4`, `l1` advances (now None)
   - `l2.val = 4`, `total = 8`, `l2` advances (now None)
   - `num = 8 % 10 = 8`, `carry = 8 // 10 = 0`
   - We add `ListNode(8)` to the result list

5. The loop ends as both lists have been traversed and there is no carry.

6. We return `res.next` (the node after dummy), which is the head of the result list: `[7,0,8]` representing 807.
