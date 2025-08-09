def findMissingNumber(numbers):
    """
    Find the missing number from a list containing numbers 1 to n with one missing.
    Uses mathematical sum formula: sum(1 to n) = n*(n+1)/2
    
    Args:
        numbers (list): List of integers from 1 to n with one number missing
        
    Returns:
        int: The missing number
        
    Raises:
        ValueError: If list is empty or invalid
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    n = len(numbers) + 1  # Original length before one number was removed
    expected_sum = n * (n + 1) // 2  # Sum of 1 to n
    actual_sum = sum(numbers)
    
    return expected_sum - actual_sum


def findMissingNumberXOR(numbers):
    """
    Find missing number using XOR operation.
    XOR property: a ^ a = 0, a ^ 0 = a
    XOR all numbers 1 to n, then XOR with all numbers in list.
    
    Args:
        numbers (list): List of integers from 1 to n with one missing
        
    Returns:
        int: The missing number
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    n = len(numbers) + 1
    xor_all = 0
    xor_present = 0
    
    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i
    
    # XOR all numbers present in the list
    for num in numbers:
        xor_present ^= num
    
    # The missing number
    return xor_all ^ xor_present


def findMissingNumberSet(numbers):
    """
    Find missing number using set difference.
    
    Args:
        numbers (list): List of integers from 1 to n with one missing
        
    Returns:
        int: The missing number
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    n = len(numbers) + 1
    complete_set = set(range(1, n + 1))
    present_set = set(numbers)
    
    missing = complete_set - present_set
    return missing.pop()


def findMissingNumberBinarySearch(numbers):
    """
    Find missing number using binary search (requires sorted list).
    
    Args:
        numbers (list): Sorted list of integers from 1 to n with one missing
        
    Returns:
        int: The missing number
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Sort the list if not already sorted
    numbers = sorted(numbers)
    
    left, right = 0, len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If numbers[mid] = mid + 1, missing number is on the right
        if numbers[mid] == mid + 1:
            left = mid + 1
        else:
            # Missing number is on the left or is mid + 1
            right = mid - 1
    
    return left + 1


def findMissingNumberIndex(numbers):
    """
    Find missing number by checking index vs value relationship.
    
    Args:
        numbers (list): Sorted list of integers from 1 to n with one missing
        
    Returns:
        int: The missing number
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Sort the list if not already sorted
    numbers = sorted(numbers)
    
    # Check each position
    for i, num in enumerate(numbers):
        if num != i + 1:
            return i + 1
    
    # If we reach here, missing number is the last one
    return len(numbers) + 1


def findMultipleMissingNumbers(numbers, n):
    """
    Bonus: Find multiple missing numbers from 1 to n.
    
    Args:
        numbers (list): List of integers with some numbers missing
        n (int): The upper bound (complete range is 1 to n)
        
    Returns:
        list: All missing numbers
    """
    complete_set = set(range(1, n + 1))
    present_set = set(numbers)
    missing = complete_set - present_set
    return sorted(list(missing))


# Performance comparison function
def comparePerformance():
    """
    Compare the performance of different methods.
    """
    import time
    import random
    
    # Create a large test case
    n = 100000
    complete_list = list(range(1, n + 1))
    missing_index = random.randint(0, n - 1)
    test_list = complete_list[:missing_index] + complete_list[missing_index + 1:]
    expected_missing = complete_list[missing_index]
    
    methods = [
        ("Sum Formula", findMissingNumber),
        ("XOR Method", findMissingNumberXOR),
        ("Set Difference", findMissingNumberSet),
    ]
    
    print(f"Performance test with n={n}, missing number={expected_missing}")
    print("-" * 60)
    
    for name, func in methods:
        start_time = time.time()
        result = func(test_list)
        end_time = time.time()
        
        print(f"{name:15s}: {result:6d} | Time: {end_time - start_time:.6f}s")


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 5], 3),           # Missing 3
        ([2, 3, 4, 5], 1),           # Missing 1 (first)
        ([1, 2, 3, 4], 5),           # Missing 5 (last)
        ([1, 3, 4, 5, 6], 2),        # Missing 2
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 1),  # Missing first in larger list
        ([1, 2, 3, 4, 5, 6, 8, 9, 10], 7),  # Missing middle in larger list
    ]
    
    print("Testing Find Missing Number Functions:")
    print("=" * 70)
    
    for i, (test_list, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: {test_list} (Expected missing: {expected})")
        
        try:
            result1 = findMissingNumber(test_list)
            result2 = findMissingNumberXOR(test_list)
            result3 = findMissingNumberSet(test_list)
            result4 = findMissingNumberBinarySearch(test_list)
            result5 = findMissingNumberIndex(test_list)
            
            print(f"  Sum formula:     {result1}")
            print(f"  XOR method:      {result2}")
            print(f"  Set difference:  {result3}")
            print(f"  Binary search:   {result4}")
            print(f"  Index check:     {result5}")
            print(f"  All correct:     {all(r == expected for r in [result1, result2, result3, result4, result5])}")
            
        except Exception as e:
            print(f"  Error: {e}")
        
        print()
    
    # Test multiple missing numbers
    print("Testing multiple missing numbers:")
    test_multiple = [1, 3, 5, 7, 9]  # Missing 2, 4, 6, 8, 10 from 1-10
    missing_multiple = findMultipleMissingNumbers(test_multiple, 10)
    print(f"Numbers present: {test_multiple}")
    print(f"Missing numbers: {missing_multiple}")
    print()
    
    # Performance comparison
    print("Performance Comparison:")
    comparePerformance()