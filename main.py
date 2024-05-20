from Components import *
import sys


def main(type: str, fileName: str):
    try:
        tell, query = ReadFile().readAll(fn=fileName)
        print("Tell: ", tell)
        print("Query: ", query)
    except:
        raise FileNotFoundError("File not found.")

    if len(tell) == 0:
        raise ValueError("No tell found.")

    if len(query) == 0:
        raise ValueError("No query found.")
    if type == "TT":
        kb = KnowledgeBase(tell, KBType.GS)
        solution = TruthTable(kb)
        print(solution.entails(query))
    elif type == "FC":
        kb = KnowledgeBase(tell, KBType.HF)
        solution = ForwardChaining(kb)
        print(solution.entails(query))
    elif type == "BC":
        kb = KnowledgeBase(tell, KBType.HF)
        solution = BackwardChaining(kb)
        print(solution.entails(query))
    else:
        raise ValueError("Invalid type.")


if __name__ == "__main__":
    # main(sys.argv[1], sys.argv[2])
    main("BC", "./Components/Datasets/test_hornKB.txt")
