import math


def countDigits(n):
    """
    Count the number of digits in a number using division method.
    
    Args:
        n (int): The number to count digits for
        
    Returns:
        int: Number of digits in the number
    """
    # Handle negative numbers
    n = abs(n)
    
    # Special case: 0 has 1 digit
    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    
    return count


def countDigitsLog(n):
    """
    Count digits using logarithm method (most efficient).
    
    Args:
        n (int): The number to count digits for
        
    Returns:
        int: Number of digits in the number
    """
    # Handle negative numbers
    n = abs(n)
    
    # Special case: 0 has 1 digit
    if n == 0:
        return 1
    
    # Number of digits = floor(log10(n)) + 1
    return math.floor(math.log10(n)) + 1


def countDigitsRecursive(n):
    """
    Count digits using recursion.
    
    Args:
        n (int): The number to count digits for
        
    Returns:
        int: Number of digits in the number
    """
    # Handle negative numbers
    n = abs(n)
    
    # Base case
    if n < 10:
        return 1
    
    # Recursive case
    return 1 + countDigitsRecursive(n // 10)


def countDigitsPowers(n):
    """
    Count digits by comparing with powers of 10.
    
    Args:
        n (int): The number to count digits for
        
    Returns:
        int: Number of digits in the number
    """
    # Handle negative numbers
    n = abs(n)
    
    # Special case: 0 has 1 digit
    if n == 0:
        return 1
    
    power = 1
    count = 1
    
    while power <= n:
        power *= 10
        if power <= n:
            count += 1
        else:
            break
    
    return count


def countDigitsBinarySearch(n):
    """
    Count digits using binary search on powers of 10.
    Efficient for very large numbers.
    
    Args:
        n (int): The number to count digits for
        
    Returns:
        int: Number of digits in the number
    """
    # Handle negative numbers
    n = abs(n)
    
    # Special case: 0 has 1 digit
    if n == 0:
        return 1
    
    # Binary search between 1 and estimated upper bound
    left, right = 1, 20  # 20 digits should cover most cases
    
    while left < right:
        mid = (left + right) // 2
        if n < 10 ** mid:
            right = mid
        else:
            left = mid + 1
    
    return left


def countSpecificDigit(n, digit):
    """
    Count occurrences of a specific digit in a number.
    
    Args:
        n (int): The number to search in
        digit (int): The digit to count (0-9)
        
    Returns:
        int: Number of times the digit appears
    """
    if not (0 <= digit <= 9):
        raise ValueError("Digit must be between 0 and 9")
    
    n = abs(n)
    
    # Special case: counting 0 in 0
    if n == 0:
        return 1 if digit == 0 else 0
    
    count = 0
    while n > 0:
        if n % 10 == digit:
            count += 1
        n = n // 10
    
    return count


def digitFrequency(n):
    """
    Get frequency of each digit (0-9) in a number.
    
    Args:
        n (int): The number to analyze
        
    Returns:
        dict: Dictionary with digit frequencies
    """
    n = abs(n)
    frequency = {i: 0 for i in range(10)}
    
    # Special case: 0 has one '0' digit
    if n == 0:
        frequency[0] = 1
        return frequency
    
    while n > 0:
        digit = n % 10
        frequency[digit] += 1
        n = n // 10
    
    return frequency


def countEvenOddDigits(n):
    """
    Count even and odd digits separately.
    
    Args:
        n (int): The number to analyze
        
    Returns:
        tuple: (even_count, odd_count)
    """
    n = abs(n)
    even_count = 0
    odd_count = 0
    
    # Special case: 0 is even
    if n == 0:
        return (1, 0)
    
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n = n // 10
    
    return (even_count, odd_count)


def sumOfDigits(n):
    """
    Calculate the sum of all digits in a number.
    
    Args:
        n (int): The number to sum digits for
        
    Returns:
        int: Sum of all digits
    """
    n = abs(n)
    digit_sum = 0
    
    while n > 0:
        digit_sum += n % 10
        n = n // 10
    
    return digit_sum


def productOfDigits(n):
    """
    Calculate the product of all digits in a number.
    
    Args:
        n (int): The number to multiply digits for
        
    Returns:
        int: Product of all digits
    """
    n = abs(n)
    
    # Special case: if any digit is 0, product is 0
    if n == 0:
        return 0
    
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n = n // 10
    
    return product


# Performance comparison function
def comparePerformance():
    """
    Compare performance of different digit counting methods.
    """
    import time
    
    # Test with various number sizes
    test_numbers = [123, 12345, 1234567890, 10**15, 10**18]
    
    methods = [
        ("Division Loop", countDigits),
        ("Logarithm", countDigitsLog),
        ("Powers of 10", countDigitsPowers),
        ("Binary Search", countDigitsBinarySearch),
    ]
    
    print("Performance Comparison:")
    print("=" * 60)
    
    for num in test_numbers:
        print(f"\nTesting with number: {num} ({countDigitsLog(num)} digits)")
        print("-" * 50)
        
        for name, func in methods:
            start_time = time.perf_counter()
            result = func(num)
            end_time = time.perf_counter()
            
            print(f"{name:15s}: {result:2d} digits | Time: {(end_time - start_time)*1000000:.2f} μs")


# Test the functions
if __name__ == "__main__":
    test_numbers = [
        0, 5, 42, 123, 1000, 12345, 
        -123, -1000, 999999, 1000000,
        10**10, 10**15, 123456789012345
    ]
    
    print("Testing Digit Counting Functions:")
    print("=" * 80)
    
    for num in test_numbers:
        result1 = countDigits(num)
        result2 = countDigitsLog(num)
        result3 = countDigitsRecursive(num)
        result4 = countDigitsPowers(num)
        result5 = countDigitsBinarySearch(num)
        
        all_match = all(r == result1 for r in [result2, result3, result4, result5])
        status = "✓" if all_match else "✗"
        
        print(f"{num:15d} | Loop: {result1:2d} | Log: {result2:2d} | Rec: {result3:2d} | "
              f"Pow: {result4:2d} | Bin: {result5:2d} | {status}")
    
    print("\nTesting Additional Digit Functions:")
    print("=" * 50)
    
    test_num = 123450
    print(f"Number: {test_num}")
    print(f"Total digits: {countDigits(test_num)}")
    print(f"Count of digit '0': {countSpecificDigit(test_num, 0)}")
    print(f"Count of digit '3': {countSpecificDigit(test_num, 3)}")
    print(f"Even/Odd digits: {countEvenOddDigits(test_num)}")
    print(f"Sum of digits: {sumOfDigits(test_num)}")
    print(f"Product of digits: {productOfDigits(test_num)}")
    print(f"Digit frequency: {digitFrequency(test_num)}")
    
    print("\nMethod Complexity Analysis:")
    print("-" * 40)
    print("Division Loop:  O(log n) time, O(1) space")
    print("Logarithm:      O(1) time, O(1) space - FASTEST")
    print("Recursion:      O(log n) time, O(log n) space")
    print("Powers of 10:   O(log n) time, O(1) space")
    print("Binary Search:  O(log log n) time, O(1) space")
    
    # Performance comparison
    print("\n")
    comparePerformance()