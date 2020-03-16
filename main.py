""""Script to check string"""
import sys

def Stringchecker(s1, s2):
    """Function check string string s1 and s2 and returns true if follows mant to one relationship else false"""

    if len(s1) != len(s2) or len(set(s1)) < len(set(s2)):
        return False
    d  = dict()
    for idx,c in enumerate(s1):
        if not d.get(c):
            d[c] = s2[idx]
        elif d[c] != s2[idx]:
            return False
    return True

if __name__ == "__main__":
    """Call the main function"""
    if Stringchecker(sys.argv[1],sys.argv[2]):
        print("true")
    else:
        print("false")