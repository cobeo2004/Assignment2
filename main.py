from Components import *
import sys


def main(fileName: str, type: str):
    try:
        tell, query = ReadFile().readAll(fn=fileName)
        # print("Tell: ", tell)
        # print("Query: ", query)
    except:
        raise FileNotFoundError("File not found.")

    if len(tell) == 0:
        raise ValueError("No tell found.")

    if len(query) == 0:
        raise ValueError("No query found.")
    if type.lower() == "tt":
        kb = KnowledgeBase(tell, KBType.GS)
        solution = TruthTable(kb)
        print(solution.entails(query))
    elif type.lower() == "fc":
        kb = KnowledgeBase(tell, KBType.HF)
        solution = ForwardChaining(kb)
        print(solution.entails(query))
    elif type.lower() == "bc":
        kb = KnowledgeBase(tell, KBType.HF)
        solution = BackwardChaining(kb)
        print(solution.entails(query))
    else:
        raise ValueError("Invalid type.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    # main("TT", "./Components/Datasets/test_genericKB_1.txt")
