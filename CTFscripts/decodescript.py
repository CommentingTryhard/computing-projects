import hashlib

# Secret string
secret = "DLROWEHTVER"

# Reverse the transformation (add 33 to each character of the secret string)
input_string = ''.join([chr(ord(c) + 33) for c in secret])

# Print the input string
print("Input string:", input_string)

# Calculate MD5 hash of the input string
md5_hash = hashlib.md5(input_string.encode()).hexdigest()

# Print the flag
flag = f"blahaj{{{md5_hash}}}"
print("Flag:", flag)
