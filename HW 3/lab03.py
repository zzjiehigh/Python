def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    return x + multiply(x, y - 1)
def collectMultiples(intList, n):
    endList = []
    if len(intList) == 0:
        return endList
    elif len(intList) > 1:
        if intList[0] % n == 0:
            return [intList[0]] + collectMultiples(intList[1:], n)
        return collectMultiples(intList[1:], n)
    elif intList[0] % n == 0:
        return [intList[0]]
    else:
        return endList
def countVowels(s):
    Vowels = ['A','E','I','O','U','a','e','i','o','u']
    if len(s) == 0:
        return 0
    else:
        if s[0] in Vowels:
            return 1 + countVowels(s[1:])
        else:
            return 0 + countVowels(s[1:])

def reverseVowels(s):
    Vowels = ['A','E','I','O','U','a','e','i','o','u']
    if len(s) == 0:
        return ""
    else:
        if s[0] in Vowels:
            return reverseVowels(s[1:]) + s[0]
        else:
            return reverseVowels(s[1:])

def removeSubString(s, sub):
    if sub not in s or len(sub) == 0:
        return s
    else:
        if s[0:len(sub)-1] == sub[0:len(sub)-1]:
            return removeSubString(s[len(sub):], sub)
        else:
            return s[0] + removeSubString(s[1:], sub)
            
    
