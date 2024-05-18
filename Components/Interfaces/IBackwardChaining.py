from Components.Interfaces.IPropositionalLogic import IPropositionalMethod
from Components.Interfaces.IHornForm import IHornForm


class IBackwardChaining(IPropositionalMethod):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        self.knowledgeBase = knowledgeBase
        self.inferred = set()  # To keep track of already inferred symbols
        self.chain = []  # To keep the chain of inferences

    def __backward_chaining(self, query):
        pass

    def entails(self, query):
        pass
