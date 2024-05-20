
from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Interfaces.IPropositionalLogic import IPropositionalMethod


class ITruthTable(IPropositionalMethod):
    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase
        self.count = 0

    def __truth_table(self, alphabetic):
        pass

    def __check(self, alphabetic, symbols, model):
        pass

    def entails(self, query):
        pass
