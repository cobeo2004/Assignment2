from Components.Interfaces.IHornForm import IHornForm
from Components.Decorator.Export import export
import re


@export
class HornForm(IHornForm):
    def __init__(self, sentence) -> None:
        self.clause = []
        self.symbols = []
        self.sentence = sentence
        self.head = ""
        self.conjuncts = []
        self.evaluate()

    def evaluate(self):
        self.clause = re.split("(=>|&|\(|\)|~|\|\||<=>)", self.sentence)
        while "" in self.clause:
            self.clause.remove("")
        while "(" in self.clause:
            self.clause.remove("(")
        while ")" in self.clause:
            self.clause.remove(")")
        if ('~' or '||' or '<=>') in self.clause:
            raise ValueError("Sentence is not in horn form", self.clause)

        if len(self.clause) == 1:
            self.head = self.clause[0]
        else:
            index = self.clause.index('=>')
            rhs = self.clause[index + 1:]
            if len(rhs) > 1:
                raise ValueError("Error horn form format", self.clause)
            self.head = rhs[0]
            lhs = self.clause[:index]
            if (lhs[0] or lhs[-1]) == '&':
                raise ValueError("Error horn form format", self.clause)

            for i in range(len(lhs) - 1):
                if lhs[i] == lhs[i + 1]:
                    raise ValueError("Error horn form format", self.clause)
            for value in lhs:
                if value != '&':
                    self.conjuncts.extend(value)
            self.symbols = self.conjuncts.copy()

        if self.head not in self.symbols:
            self.symbols.append(self.head)
