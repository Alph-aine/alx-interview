#!/usr/bin/python3
'''UTF-8 Validation'''


def validUTF8(data):
    '''Check if an integer is utf-8 encoded'''

    # Helper function to count leading 1 bits
    def count_leading_ones(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    # Helper function to check if a byte is a following byte
    def is_following_byte(byte):
        return byte >> 6 == 0b10

    i = 0

    while i < len(data):
        leading_ones = count_leading_ones(data[i])

        if leading_ones == 0:
            i += 1
        elif (leading_ones == 2 or leading_ones > 4
              or i + leading_ones > len(data)):
            return False
        else:
            for j in range(1, leading_ones):
                if not (i + j < len(data) and is_following_byte(data[i + j])):
                    return False
            i += leading_ones

    return True
