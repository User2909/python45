a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
squares = [x if x <= 5 else a.remove(x) for x in a]
print(squares)