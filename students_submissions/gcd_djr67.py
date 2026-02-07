def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# Test cases
print(gcd(54, 24))  
print(gcd(48, 18))  
print(gcd(101, 10)) 