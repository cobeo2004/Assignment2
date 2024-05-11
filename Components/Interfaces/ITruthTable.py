from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Interfaces.IPropositionalLogic import IPropositionalLogic


class ITruthTable(IPropositionalLogic):
    def __init__(self, knowledgeBase, ):
        self.knowledgeBase = knowledgeBase

    def _entails(self, alphabetic):
        symbols = self.knowledgeBase.symbols
        for symbol in alphabetic.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        return self._entails(alphabetic, symbols, {})

    def _inspect_entail(self, alphabetic, symbols, model):
        pass

    def evaluate(self, ask):
        pass

    