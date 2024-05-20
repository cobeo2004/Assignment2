from Components.Interfaces.ILogic import IEvaluation


class ILogicalSentence(IEvaluation):
    def __init__(self, sentence) -> None:
        pass

    def formatOriginal(self, sentence):
        pass

    def evaluate(self, model):
        pass

    def formatSentence(self, sentence):
        pass

    def appendAtomic(self, index, sentence, operator):
        pass
