import argparse

parser = argparse.ArgumentParser(
    description="Display the contents of the specified file in binary format."
)
parser.add_argument(
    "filename", type=str, help="name of the file that will be displayed",
)
parser.add_argument(
    "--hex",
    action="store_true",
    default=False,
    help="display the content of the file in hexadecimal representation (default: False)",
)
parser.add_argument(
    "--offset",
    action="store",
    type=int,
    default=0,
    help="start reading after from certain offset (default: 0)",
)
parser.add_argument(
    "--columns",
    action="store",
    type=int,
    default="8",
    help="the number of columns that will be displayed (default: 8)",
)
args = parser.parse_args()

with open(args.filename, "rb") as f:
    f.seek(args.offset)
    row = 0
    col = 0
    eof = False
    while not eof:
        byte = []
        print("{0:>5}".format(row), end=":    ")
        for col in range(args.columns):
            char = f.read(1)
            if not char:
                eof = True
                break
            byte.append(char)

        for b in byte:
            print("{0:08b}".format(ord(b)), end="    ")

        if col != args.columns - 1:
            print("            " * (args.columns - col), end="")

        print("|", end="    ")
        for b in byte:
            b = b.decode()
            print(b, end="")
        print("\n")
        row += 1
