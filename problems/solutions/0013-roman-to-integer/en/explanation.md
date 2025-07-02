# Roman to Integer - Solution Explanation

## Approach: Traversing the string from right to left with conditional subtraction

This solution converts a Roman numeral into an integer based on the classical Roman numeral rules. The logic involves traversing the string from the end to the beginning and applying **subtraction** when a smaller numeral appears before a larger one.

## Algorithm Logic:

1. We create a **dictionary** that maps each Roman symbol to its corresponding integer value:
   - Example: `'I' → 1`, `'V' → 5`, `'X' → 10`, `'L' → 50`, `'C' → 100`, `'D' → 500`, `'M' → 1000`.

2. We initialize two variables:
   - `resultadoFinal` (final result): stores the accumulated sum (initially `0`);
   - `valorAntes` (previous value): stores the previous symbol's value during the loop (initially `0`).

3. We iterate through the input string `s` **from end to start**:
   - For each character `s[i]`, we get its corresponding value from the dictionary.

4. We apply Roman numeral subtraction rules:
   - If `currentValue < previousValue`, subtract `currentValue` from `resultadoFinal`.
   - Otherwise, add `currentValue` to `resultadoFinal`.

5. Update `valorAntes` with the current value for the next iteration.

6. At the end of the loop, `resultadoFinal` holds the final integer representation of the Roman numeral.

## Step-by-Step Example:

Input: `s = "MCMXCIV"`

1. `V = 5` → since `5 >= 0`, add → `result = 5`
2. `I = 1` → `1 < 5`, subtract → `result = 4`
3. `C = 100` → `100 > 1`, add → `result = 104`
4. `X = 10` → `10 < 100`, subtract → `result = 94`
5. `M = 1000` → `1000 > 10`, add → `result = 1094`
6. `C = 100` → `100 < 1000`, subtract → `result = 994`
7. `M = 1000` → `1000 > 100`, add → `result = 1994`

**Final result: `1994`**

## Complexity:

- **Time:** O(n), where n is the length of the string `s`.
- **Space:** O(1), since the dictionary has a fixed size and only scalar variables are used.
