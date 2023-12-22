def calculate_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: Mean of the numbers.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float: Median of the numbers.
    """
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median_value = (middle1 + middle2) / 2
    else:
        median_value = sorted_numbers[n // 2]

    return median_value

def calculate_mode(numbers):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    list: List of modes (can be empty if no mode exists).
    """
    if not numbers:
        return None

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]

    return mode[0]

# Example usage:
# numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]
# mean_result = calculate_mean(numbers)
# median_result = calculate_median(numbers)
# mode_result = calculate_mode(numbers)

# print(f"Mean: {mean_result}")
# print(f"Median: {median_result}")
# print(f"Mode: {mode_result}")