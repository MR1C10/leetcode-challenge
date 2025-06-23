# 1. Two Sum - Solution Explanation

## Approach: Using Hash Table (Dictionary)

The solution uses a hash table data structure to solve the problem in a single pass through the array elements.

## Algorithm Logic:

1. We create an empty dictionary `num_to_index` that will map each number in the array to its index.
2. We iterate through the `nums` array with a loop.
3. For each current number (`num`):
   - We calculate the "complement" (`target - num`) which, when added to the current number, would result in the target value.
   - We check if this complement has been seen before (is in the dictionary).
   - If we find the complement, we return the indices of the two numbers.
   - Otherwise, we store the current number and its index in the dictionary for future lookups.

## Step-by-Step Example:

Using the example: `nums = [2, 7, 11, 15]`, `target = 9`

1. Initialize `num_to_index = {}`
2. Iteration 1:
   - `num = 2`, `complement = 9 - 2 = 7`
   - `7` is not in `num_to_index`
   - Add `num_to_index[2] = 0`
3. Iteration 2:
   - `num = 7`, `complement = 9 - 7 = 2`
   - `2` is in `num_to_index` with value `0`
   - Return `[0, 1]` (indices of numbers 2 and 7)
