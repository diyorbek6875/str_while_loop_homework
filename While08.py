def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    b=0
    i=0
    while i<a:
        if s[i]=="1" or s[i]=='3' or s[i]=='5' or s[i]=='7' or s[i]=='9':
            b=b+1
        i=i+1

    return b
s=input()
print(main(s))