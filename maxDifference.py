def maxDifference(arr):
    """
    Find maximum difference between two elements where larger element comes after smaller.
    Uses single pass tracking minimum element seen so far.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        int/float: Maximum difference, or None if no valid pair exists
        
    Raises:
        ValueError: If list has fewer than 2 elements
    """
    if len(arr) < 2:
        raise ValueError("List must have at least 2 elements")
    
    min_so_far = arr[0]
    max_diff = float('-inf')
    
    for i in range(1, len(arr)):
        # Calculate difference with current minimum
        current_diff = arr[i] - min_so_far
        max_diff = max(max_diff, current_diff)
        
        # Update minimum if current element is smaller
        min_so_far = min(min_so_far, arr[i])
    
    return max_diff if max_diff > float('-inf') else None


def maxDifferenceBruteForce(arr):
    """
    Brute force approach - check all valid pairs.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        int/float: Maximum difference, or None if no valid pair exists
    """
    if len(arr) < 2:
        raise ValueError("List must have at least 2 elements")
    
    max_diff = float('-inf')
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[j] - arr[i]
            max_diff = max(max_diff, diff)
    
    return max_diff if max_diff > float('-inf') else None


def maxDifferenceWithIndices(arr):
    """
    Find maximum difference and return the indices of the elements.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        tuple: (max_difference, min_index, max_index) or (None, -1, -1)
    """
    if len(arr) < 2:
        return (None, -1, -1)
    
    min_so_far = arr[0]
    min_index = 0
    max_diff = float('-inf')
    best_min_index = 0
    best_max_index = 1
    
    for i in range(1, len(arr)):
        current_diff = arr[i] - min_so_far
        
        if current_diff > max_diff:
            max_diff = current_diff
            best_min_index = min_index
            best_max_index = i
        
        if arr[i] < min_so_far:
            min_so_far = arr[i]
            min_index = i
    
    return (max_diff, best_min_index, best_max_index)


def maxDifferenceStack(arr):
    """
    Find maximum difference using stack-based approach.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        int/float: Maximum difference, or None if no valid pair exists
    """
    if len(arr) < 2:
        raise ValueError("List must have at least 2 elements")
    
    stack = []  # Will store indices
    max_diff = float('-inf')
    
    for i in range(len(arr)):
        # Remove elements from stack that are greater than current element
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        # Calculate difference with all remaining elements in stack
        for j in stack:
            diff = arr[i] - arr[j]
            max_diff = max(max_diff, diff)
        
        stack.append(i)
    
    return max_diff if max_diff > float('-inf') else None


def maxProfitStock(prices):
    """
    Stock trading variation: find maximum profit from buying and selling.
    Same as max difference but with meaningful variable names.
    
    Args:
        prices (list): List of stock prices over time
        
    Returns:
        float: Maximum profit possible
    """
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Calculate profit if we sell at current price
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        
        # Update minimum price seen so far
        min_price = min(min_price, price)
    
    return max_profit


def maxDifferenceSubarray(arr):
    """
    Find maximum difference considering all possible subarrays.
    Returns max difference between any two elements in any subarray.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        int/float: Maximum difference in any subarray
    """
    if len(arr) < 2:
        return 0
    
    global_max_diff = float('-inf')
    
    for i in range(len(arr)):
        min_in_subarray = arr[i]
        max_in_subarray = arr[i]
        
        for j in range(i + 1, len(arr)):
            min_in_subarray = min(min_in_subarray, arr[j])
            max_in_subarray = max(max_in_subarray, arr[j])
            
            current_diff = max_in_subarray - min_in_subarray
            global_max_diff = max(global_max_diff, current_diff)
    
    return global_max_diff


def analyzeArrayDifferences(arr):
    """
    Comprehensive analysis of array differences.
    
    Args:
        arr (list): List of numbers
        
    Returns:
        dict: Dictionary with various difference statistics
    """
    if len(arr) < 2:
        return {"error": "Need at least 2 elements"}
    
    max_diff_result = maxDifferenceWithIndices(arr)
    
    return {
        "max_difference": max_diff_result[0],
        "max_diff_indices": (max_diff_result[1], max_diff_result[2]),
        "max_diff_values": (arr[max_diff_result[1]], arr[max_diff_result[2]]) if max_diff_result[0] is not None else (None, None),
        "min_element": min(arr),
        "max_element": max(arr),
        "overall_range": max(arr) - min(arr),
        "array_length": len(arr),
    }


# Test the functions
if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],         # Expected: 5 (1 to 6)
        [1, 2, 3, 4, 5],            # Expected: 4 (1 to 5)
        [5, 4, 3, 2, 1],            # Expected: -1 (5 to 4, best we can do)
        [2, 7, 1, 9, 3],            # Expected: 8 (1 to 9)
        [10, 20, 30],               # Expected: 20 (10 to 30)
        [30, 20, 10],               # Expected: -10 (30 to 20, best we can do)
        [5, 5, 5, 5],               # Expected: 0 (all same)
        [1, 100],                   # Expected: 99 (1 to 100)
        [100, 1],                   # Expected: -99 (100 to 1)
    ]
    
    print("Testing Maximum Difference Functions:")
    print("=" * 80)
    
    for i, test_list in enumerate(test_cases, 1):
        print(f"Test {i}: {test_list}")
        
        try:
            result1 = maxDifference(test_list)
            result2 = maxDifferenceBruteForce(test_list)
            result3 = maxDifferenceWithIndices(test_list)
            result4 = maxDifferenceStack(test_list)
            
            print(f"  Optimized:       {result1}")
            print(f"  Brute force:     {result2}")
            print(f"  With indices:    {result3}")
            print(f"  Stack method:    {result4}")
            print(f"  Results match:   {result1 == result2 == result3[0] == result4}")
            
            if result3[0] is not None:
                min_idx, max_idx = result3[1], result3[2]
                print(f"  Best pair: arr[{min_idx}]={test_list[min_idx]} to arr[{max_idx}]={test_list[max_idx]}")
            
        except Exception as e:
            print(f"  Error: {e}")
        
        print()
    
    # Stock trading example
    print("Stock Trading Example:")
    print("-" * 30)
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = maxProfitStock(stock_prices)
    print(f"Stock prices: {stock_prices}")
    print(f"Maximum profit: ${profit}")
    
    # Comprehensive analysis
    print("\nComprehensive Analysis:")
    print("-" * 30)
    analysis_data = [2, 7, 1, 9, 3]
    analysis = analyzeArrayDifferences(analysis_data)
    print(f"Array: {analysis_data}")
    for key, value in analysis.items():
        print(f"  {key}: {value}")
    
    print("\nTime Complexity Summary:")
    print("-" * 40)
    print("Optimized (Single Pass): O(n) time, O(1) space - BEST")
    print("Seen Set:                O(n) time, O(n) space - Early exit")
    print("Stack Method:            O(n) time, O(n) space - Alternative")
    print("Brute Force:             O(n²) time, O(1) space - Slow")
    print("With Indices:            O(n) time, O(1) space - Best + info")