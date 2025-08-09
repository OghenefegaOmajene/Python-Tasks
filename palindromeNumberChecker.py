def isPalindrome(n):
    """
    Check if a number is a palindrome without converting to string.
    Uses digit reversal method.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if n < 0:
        return False
    
    # Single digit numbers are palindromes
    if n < 10:
        return True
    
    original = n
    reversed_num = 0
    
    # Reverse the number
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    # Compare original with reversed
    return original == reversed_num


def isPalindromeHalfReverse(n):
    """
    Optimized version that only reverses half the number.
    More efficient for large numbers.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if n < 0:
        return False
    
    # Single digit numbers are palindromes
    if n < 10:
        return True
    
    # Numbers ending in 0 (except 0 itself) cannot be palindromes
    if n % 10 == 0:
        return False
    
    reversed_half = 0
    
    # Reverse only half the digits
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n = n // 10
    
    # For even number of digits: n == reversed_half
    # For odd number of digits: n == reversed_half // 10
    return n == reversed_half or n == reversed_half // 10


def isPalindromeRecursive(n, power=None):
    """
    Recursive approach to check palindrome.
    
    Args:
        n (int): The number to check
        power (int): Power of 10 for the most significant digit
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    if n < 0:
        return False
    
    if n < 10:
        return True
    
    # Calculate the power for the most significant digit
    if power is None:
        temp = n
        power = 1
        while temp >= 10:
            power *= 10
            temp //= 10
    
    # Get first and last digits
    first_digit = n // power
    last_digit = n % 10
    
    # If first and last digits don't match, not a palindrome
    if first_digit != last_digit:
        return False
    
    # Remove first and last digits and check the middle part
    middle = (n % power) // 10
    return isPalindromeRecursive(middle, power // 100)


def isPalindromeDigitArray(n):
    """
    Extract digits into array and check palindrome property.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    if n < 0:
        return False
    
    if n < 10:
        return True
    
    # Extract digits into a list
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    
    # Check if the list is equal to its reverse
    # digits is already in reverse order, so check if it equals its reverse
    return digits == digits[::-1]


def isPalindromeTwoPointers(n):
    """
    Two-pointer approach using digit extraction.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    if n < 0:
        return False
    
    if n < 10:
        return True
    
    # Extract all digits
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    
    # Reverse the digits list to get correct order
    digits = digits[::-1]
    
    # Use two pointers
    left, right = 0, len(digits) - 1
    
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    
    return True


def findPalindromes(start, end):
    """
    Find all palindromes in a given range.
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
        
    Returns:
        list: All palindromic numbers in the range
    """
    palindromes = []
    for num in range(start, end + 1):
        if isPalindrome(num):
            palindromes.append(num)
    return palindromes


def nextPalindrome(n):
    """
    Find the next palindrome after a given number.
    
    Args:
        n (int): Starting number
        
    Returns:
        int: Next palindromic number
    """
    n += 1
    while not isPalindrome(n):
        n += 1
    return n


# Test the functions
if __name__ == "__main__":
    test_numbers = [
        121, 1221, 12321, 123321,  # Palindromes
        123, 1234, 12345,          # Non-palindromes
        0, 5, 9,                   # Single digits
        10, 100, 1000,             # Numbers ending in 0
        -121, -12321,              # Negative numbers
        11, 22, 33, 44, 55, 66, 77, 88, 99,  # Two-digit palindromes
    ]
    
    print("Testing Palindrome Functions:")
    print("=" * 80)
    
    for num in test_numbers:
        result1 = isPalindrome(num)
        result2 = isPalindromeHalfReverse(num)
        result3 = isPalindromeRecursive(num)
        result4 = isPalindromeDigitArray(num)
        result5 = isPalindromeTwoPointers(num)
        
        all_match = all(r == result1 for r in [result2, result3, result4, result5])
        status = "✓" if all_match else "✗"
        
        print(f"{num:6d} | Full: {result1} | Half: {result2} | Rec: {result3} | "
              f"Array: {result4} | Two-ptr: {result5} | Match: {status}")
    
    print("\nFinding palindromes in range 100-200:")
    palindromes_100_200 = findPalindromes(100, 200)
    print(f"Palindromes: {palindromes_100_200}")
    
    print("\nNext palindromes:")
    test_next = [100, 121, 999, 1991]
    for num in test_next:
        next_pal = nextPalindrome(num)
        print(f"Next palindrome after {num}: {next_pal}")
    
    print("\nPerformance Analysis:")
    print("-" * 40)
    print("Method Complexity:")
    print("  Full Reverse:    O(log n) time, O(1) space")
    print("  Half Reverse:    O(log n) time, O(1) space - FASTEST")
    print("  Recursive:       O(log n) time, O(log n) space")
    print("  Digit Array:     O(log n) time, O(log n) space")
    print("  Two Pointers:    O(log n) time, O(log n) space")