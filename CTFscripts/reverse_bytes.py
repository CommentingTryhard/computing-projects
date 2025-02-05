import sys

def reverse_every_4_bytes(input_file, output_file):
    try:
        with open(input_file, 'rb') as infile:
            data = infile.read()

        # Reverse every 4 bytes
        reversed_data = bytearray()
        for i in range(0, len(data), 4):
            reversed_data.extend(data[i:i+4][::-1])

        with open(output_file, 'wb') as outfile:
            outfile.write(reversed_data)

        print(f"Successfully reversed every 4 bytes of '{input_file}' and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python reverse_bytes.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        reverse_every_4_bytes(input_file, output_file)
