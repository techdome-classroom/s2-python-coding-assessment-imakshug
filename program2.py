class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0  # This will track the value of the previous numeral

        # Traverse the Roman numeral string from left to right
        for char in s:
            current_value = roman_values[char]
            # If the previous value is less than the current value, subtract the previous value
            if prev_value < current_value:
                total += current_value - 2 * prev_value  # Subtract prev_value twice (once for the previous addition and now for the actual subtraction)
            else:
                total += current_value
            prev_value = current_value  # Update the previous value for the next iteration

        return total
