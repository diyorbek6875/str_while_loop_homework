def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=str(s)
    i=0
    b=len(a)
    sum=0
    while i<b:
        sum=sum+int(s[i])
        i=i+1

    return sum
s=input()
print(main(s))