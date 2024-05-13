from Components.Decorator.Export import export
from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Interfaces.ITruthTable import ITruthTable


@export
class TruthTable(ITruthTable):
    def __init__(self, knowledgeBase):
        super().__init__(knowledgeBase)
        

    def _inspect_entail(self, alphabetic, symbols, model):
        if len(symbols) == 0:
            # If symbols list is empty, the model is complete
            all_true = all(sentence.solve(model) for sentence in self.kb.sentences)
            if all_true:
                # If knowledge base (kb) is true for the model
                alpha_solution = alphabetic.solve(model)
                if alpha_solution:
                    self.count += 1
                return alpha_solution
            else:
                # If knowledge base (kb) is false, the model doesn't matter for alpha
                return True
        else:
            # Recursive process for each symbol
            p = symbols[0]
            rest = symbols[1:]
            model1 = model.copy()
            model1.update({p: True})  # Add symbol where it's true to the model
            model2 = model.copy()
            model2.update({p: False})  # Add symbol where it's false to the model
            # Recursively check for all combinations of truth values for symbols
            return (self._inspect_entail(alphabetic, rest, model1) and 
                    self._inspect_entail(alphabetic, rest, model2))

    def entails(self, alphabetic):
        symbols = self.knowledgeBase.symbols
        for symbol in alphabetic.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        return self.entails(alphabetic, symbols, {})

    def evaluate(self, ask):
        alphabetic = ILogicalSentence (ask)   
        solution_found = self.__tt_entails(alphabetic)
        solution = "YES: " + str(self.count) if solution_found else "NO"
        return solution

