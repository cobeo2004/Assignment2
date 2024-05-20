from Components.Interfaces.IHornForm import IHornForm
from Components.Decorator.Export import export
import re


@export
class HornForm(IHornForm):
    def __init__(self, sentence) -> None:
        self.clauses = []
        self.symbols = set()  # Use a set to avoid duplicates
        self.sentence = sentence
        self.head = ""
        self.conjuncts = []
        self.evaluate()

    def evaluate(self):
        self.clauses = re.split("(=>|&|\(|\)|~|\|\||<=>)", self.sentence)
        self.clauses = [c.strip()
                        for c in self.clauses if c.strip() and c not in "()"]

        if any(op in self.clauses for op in ['~', '||', '<=>']):
            raise ValueError("Sentence is not in horn form", self.clauses)

        if len(self.clauses) == 1:
            self.head = self.clauses[0]
            self.symbols.add(self.head)
        else:
            index = self.clauses.index('=>')
            rhs = self.clauses[index + 1:]
            if len(rhs) > 1:
                raise ValueError("Error horn form format", self.clauses)
            self.head = rhs[0]
            self.symbols.add(self.head)

            lhs = self.clauses[:index]
            if lhs[0] == '&' or lhs[-1] == '&':
                raise ValueError("Error horn form format", self.clauses)

            for i in range(len(lhs) - 1):
                if lhs[i] == '&' and lhs[i + 1] == '&':
                    raise ValueError("Error horn form format", self.clauses)
            for value in lhs:
                if value != '&':
                    self.conjuncts.append(value)
                    self.symbols.add(value)

        # Convert back to list for the final output
        self.symbols = list(self.symbols)
