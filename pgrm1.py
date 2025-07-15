def largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

# Example usage
nums = [10, 45, 23, 89, 2]
print("Largest number:", largest_number(nums))
