from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class ForwardChaining:
    """Implementation of Forward Chaining Algorithm"""
    def __init__(self, knowledge_base):
        self.kb= knowledge_base

    # forward chaining algorithm to check if kb entails query
    # algorithm starts from symbols known to be true and makes way through premises of clauses
    # until the query is reached
    def __fc_entails(self, query):
        count = {}      # dictionary of sentences and their number of premises
        inferred = {}   # dictionary of symbols and boolean values
        agenda = []     # symbols which are known to be true
        chain = []      # list used to display path of algorithm in solution
        for sentence in self.kb.sentences:
            if len(sentence.conjuncts) > 0:
                count.update({sentence:len(sentence.conjuncts)}) # update count with the sentence and number of conjuncts
            else:
                if sentence.head == query:      # return true and query if can be directly proven
                    return True, [query] 
                agenda.append(sentence.head)    # if sentence has no conjuncts, it can be assumed true

        for symbol in self.kb.symbols:
            inferred.update({symbol: False})    # set all symbols to false initially

        while len(agenda) != 0:
            p = agenda.pop(0)       # get first propositonal symbol in agenda list
            chain.append(p)
            if not inferred[p]:     # if symbol has not yet been inferred
                inferred[p] = True
                for c in count:             # loop through all sentence (c) in count
                    if p in c.conjuncts:    # if the current agenda symbol is premise of a sentence, reduce the count by 1
                        count[c]-=1
                        if count[c] == 0:   # if the number of premises of a sentence reaches zero
                            if c.head == query:         
                                chain.append(query)
                                return True, chain      # return true if the head of clause is the query
                            agenda.append(c.head)       # if head is not query, add to agenda list
        return False, [] 

    # used solve kb entails query with forward chaining and return a string solution to print
    def solve(self, query):
        solution_found, chain = self.__fc_entails(query)
        if solution_found:
            solution = "YES: "
            for ele in chain:
                if ele is chain[-1]:
                    solution += ele
                else:
                    solution += ele + ", "
        else:
            solution = "NO"
        return solution