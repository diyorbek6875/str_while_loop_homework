def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=len(s)
    b=0
    i=0
    while i<a:
        if s[i]=="2" or s[i]=='4' or s[i]=='6' or s[i]=='8' or s[i]=='0':
            b=b+1
        i=i+1

    return b
s=input()
print(main(s))
