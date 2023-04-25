def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x = 0
    y = 0
    while len(s) >y:
        if int(s[y]) % 2 == 1:
            x += int(s[y])
        y+=1
    return x
print(main("123456"))