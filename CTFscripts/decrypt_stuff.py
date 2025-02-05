def RC4_KeySchedule(key, S):
    j = 0
    for i in range(len(key)):
        j = (j + S[i] + key[i]) % 16
        S[i], S[j] = S[j], S[i]
    return S

def decrypt(ciphertext, key):
    state = RC4_KeySchedule(key, list(range(16)))  # Initialize state
    output = []
    for i in range(len(ciphertext)):
        s = state[i % len(state)]
        output.append(ciphertext[i] ^ s)  # XOR to decrypt
        if i % len(state) == 0:
            state = RC4_KeySchedule(state, state)  # Update state
    return bytes(output)

# The provided ciphertext
ct = [
    83, 103, 109, 44, 99, 106, 98, 96, 32, 104, 122, 43, 96, 97, 107, 102,
    101, 105, 124, 110, 56, 106, 127, 80, 99, 56, 102, 53, 94, 121, 57, 119,
    119, 82, 127, 125, 62, 113, 102, 88, 58, 105, 51, 118, 93, 117, 52, 95,
    121, 48, 109, 54, 113, 105, 115, 35, 116
]

from os import urandom
# Decrypt the ciphertext using the provided key
# Use the same key that was used for encryption, e.g., key = urandom(16) if you know it.
 # Replace with the actual key used for encryption

# Decrypt the ciphertext
while True:
    key = urandom(16)
    decrypted_message = decrypt(ct, key)
    if decrypted_message[:7] == ("blahaj{"):
        print(key)
        print(decrypted_message)
        break
    else:
        print(key)
    
