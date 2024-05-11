from Components.Interfaces.IPropositionalLogic import IPropositionalMethod
from Components.Interfaces.IHornForm import IHornForm


class IForwardChaining(IPropositionalMethod):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        self.knowledgeBase = knowledgeBase
        self.count = {}
        self.inferred = {}
        self.agenda = []
        self.chain = []

    def entails(self, query):
        pass
