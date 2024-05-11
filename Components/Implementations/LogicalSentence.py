from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Decorator.Export import export
import re


@export
class LogicalSentence(ILogicalSentence):
    def __init__(self, sentence) -> None:
        self.symbols = []
        self.root = []
        self.atom = {}

        self.formatOriginal(sentence)

    def formatOriginal(self, sentence):
        orig = re.split("(=>|&|\(|\)|~|\|\||<=>)", sentence)
        while "" in orig:
            orig.remove("")
        self.original = orig.copy()
        symbols = re.split("=>|&|\(|\)|~|\|\||<=>", sentence)
        while "" in symbols:
            symbols.remove("")
        self.symbols = list(set(symbols))
        self.root = self.formatSentence(orig)

    def formatSentence(self, sentence):
        while '(' in sentence:
            lhsIndex = sentence.index('(')
            countLeft = 1
            countRight = 0
            rhsIndex = 0

            for i in range(lhsIndex + 1, len(sentence)):
                if sentence[i] == '(':
                    countLeft += 1
                elif sentence[i] == ')':
                    countRight += 1
                if countLeft == countRight:
                    rhsIndex = i
                    break
            if rhsIndex == 0:
                raise ValueError(
                    "Incorrect brackets format in sentence: ", sentence)
            section = sentence[lhsIndex + 1: rhsIndex]
            section = self.formatSentence(section)
            if len(section) == 1:
                sentence[lhsIndex] = section[0]
                del sentence[lhsIndex + 1: rhsIndex + 1]
            else:
                raise ValueError("Incorrect section format: ", section)
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
        while '=>' in sentence:
            index = sentence.index('=>')
            sentence = self.appendAtomic(index, sentence, '=>')
        while '<=>' in sentence:
            index = sentence.index('<=>')
            sentence = self.appendAtomic(index, sentence, '<=>')
        return sentence

    def appendAtomic(self, index, sentence, operator):
        if operator == '~':
            tempAtomic = [sentence[index] + sentence[index + 1]]
            tempAtomicKey = "atomKey"+str(len(self.atom) + 1)
            self.atom.update({tempAtomicKey: tempAtomic})
        else:
            tempAtomic = [sentence[index - 1],
                          sentence[index], sentence[index + 1]]
            tempAtomicKey = "atomKey"+str(len(self.atom) + 1)
            self.atom.update({tempAtomicKey: tempAtomic})
        sentence[index - 1] = tempAtomicKey
        del sentence[index: index + 2]
        return sentence

    def evaluate(self, model):
        pairs = {}
        for value in self.symbols:
            if value in model:
                pairs.update({value: model[value]})
            else:
                raise ValueError("No boolean for all symbols.")
        for key in self.atom:
            if (len(self.atom[key]) == 2):
                right = pairs[self.atom[key][1]]
                pairs.update({key: not right})
            elif (len(self.atom[key]) == 3):
                left = pairs[self.atom[key][0]]
                right = pairs[self.atom[key][2]]
                if self.atom[key][1] == '&':
                    pairs.update({key: left and right})
                elif self.atom[key][1] == '||':
                    pairs.update({key: left or right})
                elif self.atom[key][1] == '=>':
                    pairs.update({key: not left or right})
                elif self.atom[key][1] == '<=>':
                    pairs.update({key: left == right})
            else:
                raise ValueError(
                    "Atomic sentence in incorrect format: ", self.atom[key])
        return pairs[self.root[0]]
