def hash(string):
    letters = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
    'i': 105,
    'j': 106,
    'k': 107,
    'l': 108,
    'm': 109,
    'n': 110,
    'o': 111,
    'p': 112,
    'q': 113,
    'r': 114,
    's': 115,
    't': 116,
    'u': 117,
    'v': 118,
    'w': 119,
    'x': 120,
    'y': 121,
    'z': 122
    }

    hash = 0
    for i in string.lower():
        if i == ' ':
            pass
        else:
            hash += letters[i]
    return hash % 100

print(hash('hi'))
print(hash('gj'))