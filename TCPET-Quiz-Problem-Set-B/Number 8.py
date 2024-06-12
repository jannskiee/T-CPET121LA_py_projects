for i in range(4, -1, -1):
    pattern = ''
    for j in range(i, -1, -1):
        pattern += '*'
    for j in range(5 - i):
        pattern += '-'
    print(pattern)
print()

for i in range(5, 0, -1):
    pattern = ''
    for j in range(i, 0, -1):
        pattern += '*'
    for j in range(5 - i):
        pattern += '-'
    print(pattern)
print()

for i in range(1, 8):
    pattern = ''
    for j in range(i):
        pattern += '*'
    print(pattern)


for i in range(6, 0, -1):
    pattern = ''
    for j in range(i):
        pattern += '*'
    print(pattern)
