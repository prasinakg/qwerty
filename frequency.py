test_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 10}

value = 10
count = 0

for i in test_dict.values():
    if i == value:
        count += 1

print(count)