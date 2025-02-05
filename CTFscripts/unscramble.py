def switch_bits(c, p1, p2):
    """
    Swap the bits at positions p1 and p2 in the binary representation of character c.
    """
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = (bit1 << shift) | (bit2 >> shift) | rest
    return result

def unscramble(scrambled):
    """
    Reverse the scrambling logic to recover the original password.
    """
    scrambled = [ord(c) for c in scrambled]  # Convert chars to their ASCII values
    for i in range(len(scrambled)):
        c = scrambled[i]
        # Apply switchBits in reverse order
        c = switch_bits(c, 6, 7)
        c = switch_bits(c, 2, 5)
        c = switch_bits(c, 3, 4)
        c = switch_bits(c, 0, 1)
        c = switch_bits(c, 4, 7)
        c = switch_bits(c, 5, 6)
        c = switch_bits(c, 0, 3)
        c = switch_bits(c, 1, 2)
        scrambled[i] = c
    return ''.join(chr(c) for c in scrambled)

# The expected scrambled array from the problem
scrambled = [
    0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
    0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
    0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2,
    0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0
]

# Convert scrambled values to a string
scrambled_string = ''.join(chr(c) for c in scrambled)

# Reverse the scrambling
original_password = unscramble(scrambled_string)

print("Original password:", original_password)