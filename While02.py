def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    b=0
    i=0
    while i<a:
        if s[i].isalpha():
            b=b+1
        i=i+1
    return b
s=input()
print(main(s))