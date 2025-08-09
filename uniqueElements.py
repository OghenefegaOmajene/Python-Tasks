def allUnique(lst):
    """
    Check if all elements in a list are unique using set comparison.
    
    Args:
        lst (list): List to check for uniqueness
        
    Returns:
        bool: True if all elements are unique, False otherwise
    """
    return len(lst) == len(set(lst))


def allUniqueLoop(lst):
    """
    Check uniqueness using nested loops (brute force approach).
    
    Args:
        lst (list): List to check for uniqueness
        
    Returns:
        bool: True if all elements are unique, False otherwise
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


def allUniqueSeen(lst):
    """
    Check uniqueness using a seen set (single pass).
    
    Args:
        lst (list): List to check for uniqueness
        
    Returns:
        bool: True if all elements are unique, False otherwise
    """
    seen = set()
    for element in lst:
        if element in seen:
            return False
        seen.add(element)
    return True


def allUniqueDict(lst):
    """
    Check uniqueness using dictionary for counting.
    
    Args:
        lst (list): List to check for uniqueness
        
    Returns:
        bool: True if all elements are unique, False otherwise
    """
    count_dict = {}
    for element in lst:
        if element in count_dict:
            return False  # Found duplicate
        count_dict[element] = 1
    return True


def allUniqueSorted(lst):
    """
    Check uniqueness by comparing adjacent elements in sorted list.
    
    Args:
        lst (list): List to check for uniqueness
        
    Returns:
        bool: True if all elements are unique, False otherwise
    """
    if len(lst) <= 1:
        return True
    
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] == sorted_lst[i + 1]:
            return False
    return True


def findDuplicates(lst):
    """
    Find all duplicate elements in a list.
    
    Args:
        lst (list): List to check for duplicates
        
    Returns:
        list: List of duplicate elements (each duplicate appears once)
    """
    seen = set()
    duplicates = set()
    
    for element in lst:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)
    
    return list(duplicates)


def getDuplicateCount(lst):
    """
    Get count of each element in the list.
    
    Args:
        lst (list): List to analyze
        
    Returns:
        dict: Dictionary with element counts
    """
    count_dict = {}
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1
    return count_dict


def getUniqueElements(lst):
    """
    Get only the unique elements (elements that appear exactly once).
    
    Args:
        lst (list): List to filter
        
    Returns:
        list: List containing only elements that appear once
    """
    count_dict = getDuplicateCount(lst)
    return [element for element, count in count_dict.items() if count == 1]


def removeDuplicates(lst, keep_order=True):
    """
    Remove duplicates from a list.
    
    Args:
        lst (list): List to remove duplicates from
        keep_order (bool): Whether to maintain original order
        
    Returns:
        list: List with duplicates removed
    """
    if keep_order:
        seen = set()
        result = []
        for element in lst:
            if element not in seen:
                result.append(element)
                seen.add(element)
        return result
    else:
        return list(set(lst))


def firstDuplicate(lst):
    """
    Find the first element that appears as a duplicate.
    
    Args:
        lst (list): List to search
        
    Returns:
        element: First duplicate element, or None if no duplicates
    """
    seen = set()
    for element in lst:
        if element in seen:
            return element
        seen.add(element)
    return None


# Performance comparison function
def comparePerformance():
    """
    Compare performance of different uniqueness checking methods.
    """
    import time
    import random
    
    # Create test data
    sizes = [100, 1000, 10000]
    
    methods = [
        ("Set Comparison", allUnique),
        ("Seen Set", allUniqueSeen),
        ("Dictionary", allUniqueDict),
        ("Nested Loops", allUniqueLoop),
        ("Sorted Adjacent", allUniqueSorted),
    ]
    
    print("Performance Comparison:")
    print("=" * 70)
    
    for size in sizes:
        # Create list with duplicates
        test_list = [random.randint(1, size // 2) for _ in range(size)]
        
        print(f"\nTesting with list size: {size}")
        print("-" * 40)
        
        for name, func in methods:
            if name == "Nested Loops" and size > 1000:
                print(f"{name:15s}: Skipped (too slow for large lists)")
                continue
                
            start_time = time.perf_counter()
            result = func(test_list)
            end_time = time.perf_counter()
            
            print(f"{name:15s}: {str(result):5s} | Time: {(end_time - start_time)*1000:.3f} ms")


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], True),           # All unique
        ([1, 2, 3, 2, 5], False),          # Has duplicate
        ([], True),                        # Empty list
        ([42], True),                      # Single element
        ([1, 1], False),                   # Two same elements
        (['a', 'b', 'c'], True),           # String elements
        ([1, 2, 'a', 'b'], True),          # Mixed types
        ([1, 2, 3, 1], False),             # Duplicate at end
        ([1.5, 2.5, 3.5], True),           # Float elements
        ([True, False, 1, 0], False),      # Boolean/int comparison (True == 1, False == 0)
    ]
    
    print("Testing All Unique Functions:")
    print("=" * 80)
    
    for i, (test_list, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: {test_list}")
        print(f"Expected: {expected}")
        
        try:
            result1 = allUnique(test_list)
            result2 = allUniqueLoop(test_list)
            result3 = allUniqueSeen(test_list)
            result4 = allUniqueDict(test_list)
            result5 = allUniqueSorted(test_list)
            
            all_match = all(r == expected for r in [result1, result2, result3, result4, result5])
            
            print(f"  Set comparison: {result1}")
            print(f"  Nested loops:   {result2}")
            print(f"  Seen set:       {result3}")
            print(f"  Dictionary:     {result4}")
            print(f"  Sorted:         {result5}")
            print(f"  All correct:    {all_match}")
            
        except Exception as e:
            print(f"  Error: {e}")
        
        print()
    
    # Test additional functions
    print("Testing Additional Functions:")
    print("=" * 50)
    
    sample_list = [1, 2, 3, 2, 4, 3, 5]
    print(f"Sample list: {sample_list}")
    print(f"Is all unique: {allUnique(sample_list)}")
    print(f"Duplicates: {findDuplicates(sample_list)}")
    print(f"Element counts: {getDuplicateCount(sample_list)}")
    print(f"Unique elements: {getUniqueElements(sample_list)}")
    print(f"Remove duplicates: {removeDuplicates(sample_list)}")
    print(f"First duplicate: {firstDuplicate(sample_list)}")
    
    print("\nTime Complexity Summary:")
    print("-" * 40)
    print("Set Comparison:  O(n) average, O(1) space")
    print("Seen Set:        O(n) average, O(n) space")
    print("Dictionary:      O(n) average, O(n) space") 
    print("Nested Loops:    O(n²) time, O(1) space")
    print("Sorted Adjacent: O(n log n) time, O(n) space")
    
    # Run performance comparison
    print("\n")
    comparePerformance()