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
            self.queryTell(value)

    def queryAsk(self, sentence):
        if self.type == KBType.GS:
            newSentence = LogicalSentence(sentence)
            print("GS Symbols: ", newSentence.symbols)
            print("GS Atomic: ", newSentence.atom)
            print("GS Root: ", newSentence.root)
            print("GS Original: ", newSentence.original)
            print("##########################")
        elif self.type == KBType.HF:
            newSentence = HornForm(sentence)
            print("HF Clause: ", newSentence.clause)
            print("HF Symbols: ", newSentence.symbols)
            print("##########################")

        self.sentences.append(newSentence)
        for value in newSentence.symbols:
            if value not in self.symbols:
                self.symbols.append(value)
