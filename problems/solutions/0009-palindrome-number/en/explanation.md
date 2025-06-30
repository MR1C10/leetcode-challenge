# Palindrome Number - Solution Explanation

## Approach: Reversing the Number Using Math Operations

The solution uses simple math operations (without converting to a string) to determine whether an integer is a palindrome — that is, whether it reads the same forwards and backwards.

## Algorithm Logic:

1. If the number is negative (`x < 0`), return `false` immediately, since negative numbers can never be palindromes (due to the `-` sign).
2. Store the original number in a variable called `original`, as we will modify `x` during the process.
3. Create a variable `reservado` (the reversed number), initially set to `0`.
4. While `x` is greater than 0:
   - Extract the last digit using `x % 10`.
   - Append this digit to the reversed number: `reservado = reservado * 10 + digit`.
   - Remove the last digit from `x` using `x /= 10`.
5. At the end, compare the reversed number (`reservado`) with the original.
   - If they are equal, the number is a palindrome.
   - Otherwise, it is not.

## Step-by-Step Example:

Using the example: `x = 121`

1. `original = 121`, `reservado = 0`
2. Iteration 1:
   - `digit = 121 % 10 = 1`
   - `reservado = 0 * 10 + 1 = 1`
   - `x = 121 / 10 = 12`
3. Iteration 2:
   - `digit = 12 % 10 = 2`
   - `reservado = 1 * 10 + 2 = 12`
   - `x = 12 / 10 = 1`
4. Iteration 3:
   - `digit = 1 % 10 = 1`
   - `reservado = 12 * 10 + 1 = 121`
   - `x = 1 / 10 = 0`
5. Final Comparison:
   - `original (121)` == `reservado (121)` → **Returns `true`**

## Complexity:

- **Time:** O(log₁₀ n), since we process each digit once.
- **Space:** O(1), as we use only scalar variables.
