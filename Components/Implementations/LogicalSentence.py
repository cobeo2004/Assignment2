from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Decorator.Export import export
import re


@export
class Sentence(ILogicalSentence):
    def __init__(self, sentence) -> None:
        self.symbols = []
        self.root = []
        self.atomic = {}
        self.preprocessSentence(sentence)

    def preprocessSentence(self, sentence):
        original = re.split("(=>|&|\(|\)|~|\|\||<=>)", sentence)
        while "" in original:
            original.remove("")
        self.original = original.copy()
        symbols = re.split("=>|&|\(|\)|~|\|\||<=>", sentence)
        while "" in symbols:
            symbols.remove("")
        self.symbols = list(set(symbols))
        self.root = self.formatSentence(original)

    def formatSentence(self, sentence):
        while '(' in sentence:
            lhs = sentence.index('(')
            lhs_count = 1
            rhs_count = 0

            rhs = 0
            for i in range(lhs + 1, len(sentence)):
                if sentence[i] == '(':
                    lhs_count += 1
                if sentence[i] == ')':
                    rhs_count += 1
                if lhs_count == rhs_count:
                    rhs = i
                    break
            if rhs == 0:
                raise ValueError("Unbalanced parenthesis")

            section = sentence[lhs + 1: rhs]
            section = self.formatSentence(section)

            if len(section) == 1:
                sentence[lhs] = section[0]
                del sentence[lhs + 1: rhs + 1]
            else:
                raise ValueError("Incorrect format section: ", section)

        while '~' in sentence:
            index = sentence.index('~')
            sentence = self.appendAtomic(index, sentence, '~')
        while ('&' or '||') in sentence:
            if '&' in sentence:
                index = sentence.index('&')
            if '||' in sentence:
                if sentence.index('||') < index:
                    index = sentence.index('||')
                sentence = self.appendAtomic(index, sentence, '&||')
        while ('=>') in sentence:
            index = sentence.index('=>')
            sentence = self.appendAtomic(index, sentence, '=>')
        while ('<=>') in sentence:
            index = sentence.index('<=>')
            sentence = self.appendAtomic(index, sentence, '<=>')
        return sentence

    def appendAtomic(self, index, sentence, connectiveSymbols):
        if connectiveSymbols == '~':
            atom = [sentence, sentence[index + 1]]
            atomKey = "atom" + str(len(self.atomic) + 1)
            self.atomic.update({atomKey: atom})
            sentence[index] = atomKey
            del sentence[index + 1]
        else:
            atom = [sentence[index - 1], sentence[index], sentence[index + 1]]
            atomKey = "atom" + str(len(self.atomic) + 1)
            self.atomic.update({atomKey: atom})
            sentence[index - 1] = atomKey
            del sentence[index: index + 2]
        return sentence

    def evaluate(self, model):
        boolPairs = {}
        for value in self.symbols:
            if value in model:
                boolPairs.update({value: model[value]})
            else:
                raise ValueError(
                    "Model does not contain boolean in all symbols.")

        for key in self.atomic:
            if len(self.atomic[key] == 2):
                rhs = boolPairs[self.atomic[key][1]]
                boolPairs.update({key: not rhs})
            elif len(self.atomic[key] == 3):
                lhs = boolPairs[self.atomic[key][0]]
                rhs = boolPairs[self.atomic[key][2]]
                if boolPairs[self.atomic[key][1]] == '&':
                    boolPairs.update({key: lhs and rhs})
                elif boolPairs[self.atomic[key][1]] == '||':
                    boolPairs.update({key: lhs or rhs})
                elif boolPairs[self.atomic[key][1]] == '=>':
                    boolPairs.update({key: not lhs or rhs})
                elif boolPairs[self.atomic[key][1]] == '<=>':
                    boolPairs.update({key: lhs == rhs})
            else:
                raise ValueError("Incorrect atomic format.", self.atomic[key])

        return boolPairs[self.root[0]]
