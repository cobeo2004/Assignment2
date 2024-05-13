from Components.Decorator.Export import export
from Components.Interfaces.ITruthTable import ITruthTable


@export
class TruthTable(ITruthTable):
    def __init__(self, knowledgeBase):
        super().__init__(knowledgeBase)

    def _inspect_entail(self, alphabetic, symbols, model):
        return super()._inspect_entail(alphabetic, symbols, model)

    def entails(self, alphabetic):
        symbols = self.knowledgeBase.symbols
        for symbol in alphabetic.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        return self.entails(alphabetic, symbols, {})
