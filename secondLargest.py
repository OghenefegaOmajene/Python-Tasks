def secondLargest(numbers):
    """
    Find the second largest number in a list without using sorting.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: The second largest number
        None: If list has fewer than 2 unique elements
        
    Raises:
        ValueError: If list is empty or contains non-numeric values
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    if len(numbers) < 2:
        return None
    
    # Initialize largest and second largest
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("List must contain only numeric values")
        
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    # If second_largest is still -inf, all elements were the same
    return second_largest if second_largest != float('-inf') else None


def secondLargestSet(numbers):
    """
    Find second largest using set to remove duplicates first.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: The second largest number
        None: If list has fewer than 2 unique elements
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Remove duplicates by converting to set, then back to list
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None
    
    # Find largest and second largest in unique numbers
    largest = max(unique_numbers)
    unique_numbers.remove(largest)
    second_largest = max(unique_numbers)
    
    return second_largest


def secondLargestTwoPass(numbers):
    """
    Find second largest using two passes through the list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: The second largest number
        None: If list has fewer than 2 unique elements
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # First pass: find the largest
    largest = max(numbers)
    
    # Second pass: find the largest that's not equal to the overall largest
    second_largest = float('-inf')
    found_second = False
    
    for num in numbers:
        if num < largest and num > second_largest:
            second_largest = num
            found_second = True
    
    return second_largest if found_second else None


def secondLargestWithIndex(numbers):
    """
    Find second largest and return both value and its first occurrence index.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        tuple: (second_largest_value, index) or (None, -1) if not found
    """
    if not numbers or len(numbers) < 2:
        return (None, -1)
    
    largest = float('-inf')
    second_largest = float('-inf')
    second_largest_index = -1
    
    for i, num in enumerate(numbers):
        if num > largest:
            if largest != float('-inf'):  # Previous largest becomes second largest
                second_largest = largest
                # Find index of previous largest (this is complex, so we'll track differently)
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            second_largest_index = i
    
    # Need to handle the case where the second largest was initially the largest
    if second_largest_index == -1 and second_largest != float('-inf'):
        # Find first occurrence of second_largest
        for i, num in enumerate(numbers):
            if num == second_largest:
                second_largest_index = i
                break
    
    return (second_largest if second_largest != float('-inf') else None, 
            second_largest_index if second_largest != float('-inf') else -1)


# Test the functions
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 2, 2, 3, 3],
        [10, 10, 10],  # All same numbers
        [42],  # Single element
        [100, 50, 75, 25, 90],
        [-5, -2, -10, -1],  # Negative numbers
        [3.14, 2.71, 1.41, 3.14],  # Floats with duplicates
        [],  # Empty list (will raise error)
    ]
    
    print("Testing Second Largest Functions:")
    print("=" * 60)
    
    for i, test_list in enumerate(test_cases):
        print(f"Test {i + 1}: {test_list}")
        
        try:
            result1 = secondLargest(test_list)
            result2 = secondLargestSet(test_list)
            result3 = secondLargestTwoPass(test_list)
            result4 = secondLargestWithIndex(test_list)
            
            print(f"  Single pass:     {result1}")
            print(f"  Using set:       {result2}")
            print(f"  Two pass:        {result3}")
            print(f"  With index:      {result4}")
            print(f"  All match:       {result1 == result2 == result3 == result4[0]}")
            
        except ValueError as e:
            print(f"  Error: {e}")
        
        print()