def reverseNumber(n):
    """
    Reverse the digits of a number without converting to string.
    
    Args:
        n (int): The number to reverse
        
    Returns:
        int: The number with digits reversed
    """
    # Handle negative numbers
    is_negative = n < 0
    n = abs(n)
    
    reversed_num = 0
    
    while n > 0:
        # Get the last digit
        digit = n % 10
        # Add it to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from original number
        n = n // 10
    
    # Apply the original sign
    return -reversed_num if is_negative else reversed_num


def reverseNumberRecursive(n, reversed_num=0):
    """
    Recursive version of number reversal.
    
    Args:
        n (int): The number to reverse
        reversed_num (int): Accumulator for the reversed number
        
    Returns:
        int: The number with digits reversed
    """
    # Handle negative numbers
    if n < 0:
        return -reverseNumberRecursive(-n, 0)
    
    # Base case
    if n == 0:
        return reversed_num
    
    # Recursive case
    return reverseNumberRecursive(n // 10, reversed_num * 10 + n % 10)


# Test the functions
if __name__ == "__main__":
    test_cases = [123, 4560, 789, -123, -4560, 0, 7, -7, 1000, 10203]
    
    print("Testing reverseNumber function (iterative):")
    print("-" * 50)
    for num in test_cases:
        result = reverseNumber(num)
        print(f"reverseNumber({num:6d}) = {result:6d}")
    
    print("\nTesting reverseNumberRecursive function:")
    print("-" * 50)
    for num in test_cases:
        result = reverseNumberRecursive(num)
        print(f"reverseNumberRecursive({num:6d}) = {result:6d}")