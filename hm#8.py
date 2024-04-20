def second_smallest(numbers):
    if len(numbers) < 2:
        return "The set of numbers is too small"
    numbers = sorted(numbers)
    return numbers[1]
assert second_smallest([4, 5, 1, 3, 2]) == 2, "First check failed"
print("All checks passed successfully!")
