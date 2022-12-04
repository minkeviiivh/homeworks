a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
data = set(list(a.keys()) + list(b.keys()))
result = {}
for key in data:
    if key in a:
        value_ftr = a[key]
        if value_past := result.get(key, None):
            result[key] = [value_ftr[0], value_past]
        else:
            result[key] = [value_ftr, None]
    if key in b:
        value_ftr = b[key]
<<<<<<< HEAD
        if value_past := result.get(key, None):
            result[key] = [value_past[0], value_ftr]
        else:
            result[key] = [None, value_ftr]
=======
        result[key] = [a.get(key), b.get(key)]
>>>>>>> 6019c970bd3f7be81dc5c0b9866de6646fc927f7
print(result)
