from Components.Interfaces.ILogic import IMethod


class ITruthTable(IMethod):
    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase
        self.count = 0

    def __truth_table(self, alphabetic):
        pass

    def __check(self, alphabetic, symbols, model):
        pass

    def entails(self, query):
        pass
