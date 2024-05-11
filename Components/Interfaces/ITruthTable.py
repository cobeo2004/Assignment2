from Components.Interfaces.IPropositionalLogic import IPropositionalLogic


class ITruthTable(IPropositionalLogic):
    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase

    def _entails(self, alphabetic):
        pass

    def _inspect_entail(self, alphabetic, symbols, model):
        pass

    def evaluate(self, ask):
        pass
