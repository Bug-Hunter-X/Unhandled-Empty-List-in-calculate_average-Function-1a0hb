def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (bug introduced here):
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10, 20, 30]
average = calculate_average(my_list) #This will not throw an error
print(f"The average is: {average}")