# Write a function that takes an integer and returns:
# - 'Even and divisible by 3' if it's both even and divisible by 3,
# - 'Even' if only even,
# - 'Odd' if it's odd,
# - 'Zero' if it’s 0.

def digitClassifier(n):
    """
    Classify an integer based on its properties.
    
    Args:
        n (int): The integer to classify
        
    Returns:
        str: Classification string based on the number's properties
    """
    # Check if the number is zero first
    if n == 0:
        return 'Zero'
    
    # Check if the number is even
    if n % 2 == 0:
        # If even, check if it's also divisible by 3
        if n % 3 == 0:
            return 'Even and divisible by 3'
        else:
            return 'Even'
    else:
        # If not even, it's odd
        return 'Odd'


# Test the function with various inputs
if __name__ == "__main__":
    test_cases = [0, 1, 2, 3, 4, 5, 6, 9, 12, 15, 18, -6, -9, -12]
    
    print("Testing digitClassifier function:")
    print("-" * 40)
    for num in test_cases:
        result = digitClassifier(num)
        print(f"digitClassifier({num:3d}) = '{result}'")