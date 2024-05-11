from Components import *
import sys


def main(type: str, fileName: str):
    try:
        tell, query = ReadFile().readAll(fn=fileName)
    except:
        raise FileNotFoundError("File not found.")

    if len(tell) == 0:
        print("No tell found.")
        sys.exit(0)

    if len(query) == 0:
        print("No ask found.")
        sys.exit(0)

    if type == "TT":
        kb = KnowledgeBase(tell, KBType.GS)
    elif type == "FC":
        kb = KnowledgeBase(tell, KBType.HF)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
