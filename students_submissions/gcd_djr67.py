def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined")
        return None
    
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both a and b must be integers")
        return None
    
    if b == 0:
        return a
        
    return gcd(b, a % b)
    
# Test cases
print(gcd(54, 24))  
print(gcd(48, 18))  
print(gcd(101, 10)) 