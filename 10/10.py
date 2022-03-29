"""
1, 11, 21, 1211, ...
"""

from operator import ne
from ssl import SSL_ERROR_EOF


def series(max_num):
    current = '1'
    next = ''
    for _ in range(max_num):
        prev_char = current[0]
        char_count = 0
        next = ''
        for i in range(0, len(current)):
            if current[i] == prev_char:
                char_count+=1
            else:
                next = next + str(char_count) + prev_char
                char_count = 1
                prev_char = current[i]
        next = next + str(char_count) + prev_char
        current = next
    return current

print(len(series(30)))