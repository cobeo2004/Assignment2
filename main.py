from Components import ReadFile
import sys


def main(fn: str):
    tell, query = ReadFile().readAll(fn)
    print(tell, query)


if __name__ == "__main__":
    main(sys.argv[1])
