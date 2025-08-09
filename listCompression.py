def processEvenNumbers(numbers):
    """
    Takes a list of integers and returns a new list with even numbers doubled
    and odd numbers removed.
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        list: New list containing only doubled even numbers
    """
    result = []
    for num in numbers:
        if num % 2 == 0:  # Check if number is even
            result.append(num * 2)  # Double the even number and add to result
    return result


def processEvenNumbersListComp(numbers):
    """
    Same functionality using list comprehension.
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        list: New list containing only doubled even numbers
    """
    return [num * 2 for num in numbers if num % 2 == 0]


def processEvenNumbersFilter(numbers):
    """
    Same functionality using filter() and map().
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        list: New list containing only doubled even numbers
    """
    # First filter even numbers, then map to double them
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(map(lambda x: x * 2, even_numbers))


# Test the functions
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 6],
        [10, 15, 20, 25, 30],
        [1, 3, 5, 7, 9],  # All odd numbers
        [2, 4, 6, 8, 10], # All even numbers
        [],               # Empty list
        [0, -2, -3, -4, 7, 8],  # Including zero and negative numbers
        [100, 101, 102, 103]
    ]
    
    print("Testing processEvenNumbers function:")
    print("=" * 60)
    
    for i, test_list in enumerate(test_cases, 1):
        result1 = processEvenNumbers(test_list)
        result2 = processEvenNumbersListComp(test_list)
        result3 = processEvenNumbersFilter(test_list)
        
        print(f"Test {i}:")
        print(f"  Input:           {test_list}")
        print(f"  Result (loop):   {result1}")
        print(f"  Result (comp):   {result2}")
        print(f"  Result (filter): {result3}")
        print(f"  All match:       {result1 == result2 == result3}")
        print()