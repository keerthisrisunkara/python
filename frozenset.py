myset = {1, 2, 3, 4}
fs = frozenset(myset)
print(type(fs))
print(fs)
fs.add(5)
print(fs)  # error because frozenset is immutable
