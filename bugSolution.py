def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    return sum(numbers) / len(numbers)

# Example usage:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: The average is: 0

my_list = [10, 20, 30]
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: The average is: 20.0