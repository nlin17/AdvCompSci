def permutations(s, prefix=""):
    if len(s) == 0: 
        print(prefix)
    else:
        for i, char in enumerate(s):
            permutations(s[:i] + s[i+1:], prefix + char)
    
s = "abcdef"
permutations(s)