def pyramid_pattern(rows):
    for i in range(rows):
        # print leading spaces
        print(' ' * (rows-i), end='')
        # print stars with space
        print('* ' * (i+1))
pyramid_pattern(5)
print("                                 ")

def pyramid_reverse(rows):
    for i in range(rows,0,-1):
        # print leading spaces
        print(' ' * (rows - i), end='')
        # print stars with space
        print('* ' * (i))
pyramid_reverse(5)
print("                                 ")

def pyramid_right(rows):
    for i in range(rows):
        # print leading spaces
        print(' ' * (rows), end='')
        # print stars with space
        print('*' * (i + 1))
pyramid_right(5)
print("                                 ")

def pyramid_left(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i)+  '*' * i)

pyramid_left(5)
print("                                 ")