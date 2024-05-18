from Components.Interfaces.IKnowledgeBase import IKnowledgeBase
from Components.Decorator.Export import export
from Components.Enums.KBTypes import KBType
from Components.Implementations.LogicalSentence import LogicalSentence
from Components.Implementations.HornForm import HornForm


@export
class KnowledgeBase(IKnowledgeBase):
    def __init__(self, sentences, type: KBType) -> None:
        self.sentences = []
        self.symbols = []
        if KBType.isKBType(type):
            self.type = type
        else:
            raise ValueError("Unknown knowledge base type.")
        for value in sentences:
            self.queryAsk(value)
        # if (type == KBType.HF):
        #     print("Clauses: ", [
        #           sentence.clauses for sentence in self.sentences])
        #     print("Symbols: ", self.symbols)
        # else:
        #     print("Clauses: ", [
        #           sentence.atom for sentence in self.sentences])
        #     print("Symbols: ", self.symbols)

    def queryAsk(self, sentence):
        if self.type == KBType.GS:
            newSentence = LogicalSentence(sentence)
            # print("GS Symbols: ", newSentence.symbols)
            # print("GS Atomic: ", newSentence.atom)
            # print("GS Root: ", newSentence.root)
            # print("GS Original: ", newSentence.original)
            # print("##########################")
        elif self.type == KBType.HF:
            newSentence = HornForm(sentence)
            # print("HF Clause: ", newSentence.clauses)
            # print("HF Symbols: ", newSentence.symbols)
            # print("HF Conjunction: ", newSentence.conjuncts)
            # print("##########################")

        self.sentences.append(newSentence)
        for value in newSentence.symbols:
            if value not in self.symbols:
                self.symbols.append(value)
