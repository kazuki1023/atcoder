def count_good_numbers(N):
    """Count the number of good numbers less than or equal to N."""
    count = 0
    for num in range(1, N + 1):
        digit_sum = sum(int(digit) for digit in str(num))
        if num % digit_sum == 0:
            count += 1
    return count

# Example: Count good numbers less than or equal to a given number (smaller value for demonstration)
# For larger N, this method might still be inefficient.
N = int(input())  # Smaller value for demonstration, replace with larger N as needed
print(count_good_numbers(N))
