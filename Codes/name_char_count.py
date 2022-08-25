name = input('plz enter your name\n')
i = 0
temp = ''
while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    i += 1

# using dictionary

def word_count(s):
    char = {}
    for i in s:
        char[i] = s.count(i)
    return char

print(word_count('hameed kahn'))