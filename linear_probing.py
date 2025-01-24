# Courtesy of Ben Long

class HashTable():
    def __init__(self, size=100):
        self.table = [0] * size
    def resize(self):
        new_table = [0] * len(self.table) * 2
        for i in self.table:
            new_table.append(hash(i))
        self.table = new_table
    def display(self):
        print(self.table)
    def find(self, string):
        hash = self.hash(string)
        while self.table[hash] != string:
            hash += 1
            if hash == self.hash(string):
                self.resize()
            if hash < len(self.table):
                hash == 0
        return hash
    def insert(self, string):
        hash = self.hash(string)
        while True:
            if self.table[hash % 100] == 0:
                break
            else:
                hash += 1
        self.table[hash % 100] = string

    def hash(self, string):
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
    
table = HashTable()
table.insert('hi')
table.insert('bo')
print(table.find('hi'))
print(table.find('bo'))