from math import gcd

def gcdOfStrings(self, str1: str, str2: str) -> str:
    if (str1 + str2) != (str2 + str1):
        return ""
    divide = gcd(len(str1), len(str2))
    return str1[:divide]



