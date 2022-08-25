square = {i : i**2 for i in range(1,11)}
print(square) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

for j,k in square.items():
    print(f'{j} : {k}')

# word count
s = 'Hameed khan'

print({c : s.count(c) for c in s})

# even oddd

even_odd = {i : ('even' if i%2 == 0 else 'odd') for i in range(1,11)}
print(even_odd)