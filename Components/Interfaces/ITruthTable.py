from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Interfaces.IPropositionalLogic import IPropositionalMethod


class ITruthTable(IPropositionalMethod):
    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase

    def _inspect_entail(self, alphabetic, symbols, model):
        pass

    def entails(self, query):
        pass
