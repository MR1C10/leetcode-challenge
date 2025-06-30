# 1. Two Sum - Solution Explanation

## Approach: Using a Hash Table (Dictionary)

The solution uses a dictionary to store the numbers already seen along with their respective indices. This approach allows solving the problem in linear time **O(n)**, avoiding the comparison of all possible pairs (which would have **O(n²)** complexity).

## Algorithm Logic

1. We create an empty dictionary called `map`, which will map each number in the array to its index.
2. We iterate over the `nums` array using a `for` loop.
3. For each current number `nums[i]`:
   - We calculate the **complement**: `complement = target - nums[i]`.
   - We check if this complement already exists in the dictionary:
     - If it does, it means we found the two numbers that sum up to the target, and we return their indices: the one for the complement and the one for the current number.
     - Otherwise, we add `nums[i]` to the dictionary, associating it with index `i`.

## Step-by-Step Example

**Input:** `nums = [2, 7, 11, 15]`, `target = 9`

1. Initialize the dictionary: `map = {}`
2. Iteration 0:
   - `nums[0] = 2`
   - `complement = 9 - 2 = 7`
   - `7` is **not** in the dictionary
   - Add `2` to the dictionary: `map = { 2: 0 }`
3. Iteration 1:
   - `nums[1] = 7`
   - `complement = 9 - 7 = 2`
   - `2` **is** in the dictionary (index `0`)
   - Return `[0, 1]`

## Complexity

- **Time:** O(n), since we traverse the array only once.
- **Space:** O(n), due to the dictionary used to store seen numbers.
