#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_len = len(argv)
    result = 0

    for i in range(1, argv_len):
        result += int(argv[i])

    print("{:d}".format(result))
