from Components.Interfaces.ILogic import IMethod


class IForwardChaining(IMethod):
    def __init__(self, knowledgeBase) -> None:
        self.knowledgeBase = knowledgeBase
        self.count = {}
        self.inferred = {}
        self.agenda = []
        self.chain = []

    def entails(self, query):
        pass
