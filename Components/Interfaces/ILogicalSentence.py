from Components.Interfaces.IPropositionalLogic import IPropositionalLogic


class ILogicalSentence(IPropositionalLogic):
    def __init__(self, sentence) -> None:
        pass

    def preprocessSentence(self, sentence):
        pass

    def evaluate(self, model):
        pass

    def formatSentence(self, sentence):
        pass

    def appendAtomic(self, index, sentence, connectiveSymbols):
        pass
