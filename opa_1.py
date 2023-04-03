class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

hash = HashTable()
hash['book'] = "this is book area"
hash['game'] = "this is game area"
hash['chair'] = "this is chair area"

print(hash['book'])
# this is book area



