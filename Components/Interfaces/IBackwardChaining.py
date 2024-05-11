from Components.Interfaces.IPropositionalLogic import IPropositionalMethod
from Components.Interfaces.IHornForm import IHornForm


class IBackwardChaining(IPropositionalMethod):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        self.knowledgeBase = knowledgeBase
        self.chain = []
        self.removed = []

    def __backward_chaining(self, query):
        pass

    def entails(self, query):
        pass
