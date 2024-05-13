from Components.Decorator.Export import export
from Components.Interfaces.IBackwardChaining import IBackwardChaining
from Components.Interfaces.IHornForm import IHornForm

@export
class BackwardChaining(IBackwardChaining):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        super().__init__(knowledgeBase)
        self.knowledgeBase = knowledgeBase

    def __backward_chaining(self, query):
        pass

    def entails(self, query):
        pass

    def evaluate(self, query):
        solution_found, chain = self.__bc_entails(query)
        
        if solution_found:
            # If a solution is found
            solution = "YES: " + ", ".join(chain)
        else:
            # If no solution is found
            solution = "NO"
            
        return solution

