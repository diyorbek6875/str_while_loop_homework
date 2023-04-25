def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    a=len(s)
    b=0
    while i<a:
        if s[i].islower():
            b=b+1
        i=i+1

    return b 
s=input()
print(main(s))