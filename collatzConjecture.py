def collatzSteps(n):
    """
    Calculate the number of steps to reach 1 using the Collatz conjecture rules.
    
    Rules:
    - If n is even: n = n / 2
    - If n is odd: n = 3 * n + 1
    
    Args:
        n (int): Starting positive integer
        
    Returns:
        int: Number of steps to reach 1
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return 0
    
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Even: divide by 2
        else:
            n = 3 * n + 1  # Odd: multiply by 3 and add 1
        steps += 1
    
    return steps


def collatzSequence(n):
    """
    Generate the complete Collatz sequence for a given number.
    
    Args:
        n (int): Starting positive integer
        
    Returns:
        list: Complete sequence from n to 1
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence


def collatzStepsRecursive(n, steps=0):
    """
    Recursive version of Collatz steps calculation.
    
    Args:
        n (int): Current number in sequence
        steps (int): Current step count
        
    Returns:
        int: Total steps to reach 1
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Base case
    if n == 1:
        return steps
    
    # Recursive cases
    if n % 2 == 0:
        return collatzStepsRecursive(n // 2, steps + 1)
    else:
        return collatzStepsRecursive(3 * n + 1, steps + 1)


def findMaxSteps(limit):
    """
    Find the number (up to limit) that takes the most steps to reach 1.
    
    Args:
        limit (int): Upper limit to check
        
    Returns:
        tuple: (number, max_steps)
    """
    max_steps = 0
    max_number = 1
    
    for i in range(1, limit + 1):
        steps = collatzSteps(i)
        if steps > max_steps:
            max_steps = steps
            max_number = i
    
    return max_number, max_steps


# Test the functions
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 100]
    
    print("Collatz Conjecture - Steps to reach 1:")
    print("=" * 50)
    
    for num in test_numbers:
        steps_iter = collatzSteps(num)
        steps_rec = collatzStepsRecursive(num)
        sequence = collatzSequence(num)
        
        print(f"n = {num:3d}")
        print(f"  Steps (iterative): {steps_iter}")
        print(f"  Steps (recursive): {steps_rec}")
        print(f"  Sequence: {sequence}")
        print(f"  Sequence length: {len(sequence)}")
        print()
    
    # Find the number with maximum steps up to 100
    print("Finding number with maximum steps (up to 100):")
    max_num, max_steps = findMaxSteps(100)
    print(f"Number {max_num} takes {max_steps} steps to reach 1")
    print(f"Sequence: {collatzSequence(max_num)}")