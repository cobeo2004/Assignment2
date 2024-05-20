from Components.Interfaces.IForwardChaining import IForwardChaining
from Components.Decorator.Export import export
from Components.Interfaces.IHornForm import IHornForm


@export
class ForwardChaining(IForwardChaining):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        super().__init__(knowledgeBase)

    def __forward_chaining(self, query):
        # Clear the chain at the beginning
        self.chain.clear()

        for sentence in self.knowledgeBase.sentences:
            if len(sentence.conjuncts) == 0:
                if sentence.head == query:
                    self.chain.append(query)
                    return True
                self.agenda.append(sentence.head)
            else:
                self.count.update({sentence: len(sentence.conjuncts)})

        for symbol in self.knowledgeBase.symbols:
            self.inferred.update({symbol: False})

        while len(self.agenda) != 0:
            p = self.agenda.pop(0)
            if not self.inferred[p]:
                self.chain.append(p)
                self.inferred[p] = True
                for sentence in self.count:
                    if p in sentence.conjuncts:
                        self.count[sentence] -= 1
                        if self.count[sentence] == 0:
                            if sentence.head == query:
                                self.chain.append(sentence.head)
                                return True
                            self.agenda.append(sentence.head)

        return False

    def entails(self, query):
        isFound = self.__forward_chaining(query)
        if isFound:
            result = "YES: " + ", ".join(self.chain)
        else:
            result = "NO"
        return result
