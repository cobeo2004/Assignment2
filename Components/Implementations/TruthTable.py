from Components.Decorator.Export import export
from Components.Implementations.LogicalSentence import LogicalSentence
from Components.Interfaces.ITruthTable import ITruthTable
from Components.Debug.log import logResultToFile


@export
class TruthTable(ITruthTable):
    def __init__(self, knowledgeBase):
        super().__init__(knowledgeBase)

    def __check(self, alphabetic, symbols, model):
        if (len(symbols) == 0):
            all_eval = True
            for sentence in self.knowledgeBase.sentences:
                if not sentence.evaluate(model):
                    all_eval = False
            if all_eval:
                alpha = alphabetic.evaluate(model)
                if alpha:
                    self.count += 1
                return alpha
            else:
                return True
        else:
            firstSymbol = symbols[0]
            restSymbol = symbols[1:]
            model1 = model.copy()
            model1.update({firstSymbol: True})
            model2 = model.copy()
            model2.update({firstSymbol: False})
            return (self.__check(alphabetic, restSymbol, model1) and self.__check(alphabetic, restSymbol, model2))

    def __truth_table(self, alphabetic):
        symbols = self.knowledgeBase.symbols
        for symbol in alphabetic.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        return self.__check(alphabetic, symbols, {})

    def entails(self, query):
        alpha = LogicalSentence(query)
        solution = self.__truth_table(alpha)
        if solution:
            result = "YES: " + str(self.count)
        else:
            result = "NO"
        return result
