import argparse

parser = argparse.ArgumentParser(description="XOR encrypts a file with a key")
parser.add_argument("input", metavar="i", type=str, help="The file to decrypt")
parser.add_argument("output", metavar="o", type=str, help="Output file")
parser.add_argument("key", metavar="k", type=str, help="XOR key")

args = parser.parse_args()

with open(args.input, "rb") as file:
    data = file.read()

keys=[int(args.key[i:i+2],16) for i in range(0,len(args.key),2)]

encrypted = b""

for idx, c in enumerate(data):
    c_e = c ^ keys[idx % len(keys)]
    encrypted += c_e.to_bytes(1, 'little')

with open(args.output, 'wb') as file:
    file.write(encrypted)

print("Done encrypting file")