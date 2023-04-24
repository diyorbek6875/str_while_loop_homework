def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    a=len(s)
    while i<a:
        if s[i].isdigit():
            k=k+1

        i=i+1

    return k
s=str(input())
print(main(s))