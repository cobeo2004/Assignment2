from Components import ReadFile
import sys


def main(fileName: str):
    tell, query = ReadFile().readAll(fileName)
    print("Tell: ", tell)
    print("Query: ", query)


if __name__ == "__main__":
    main(sys.argv[1])
