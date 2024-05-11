from Components.Decorator.Export import export
from Components.Interfaces.IBackwardChaining import IBackwardChaining
from Components.Interfaces.IHornForm import IHornForm


class BackwardChaining(IBackwardChaining):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        super().__init__(knowledgeBase)

    def __backward_chaining(self, query):
        pass

    def entails(self, query):
        pass
