from Components import ReadFile
import sys


def main(fileName: str):
    tell, query = ReadFile().readAll(fileName)
    symbols, sentences = ReadFile().parseSymbolsSentences(tell)

    print("Tell: ", tell)
    print("Query: ", query)
    print("Symbols: ", symbols)
    print("Sentences: ", sentences)


if __name__ == "__main__":
    main(sys.argv[1])
