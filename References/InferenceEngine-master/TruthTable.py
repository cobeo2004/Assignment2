from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class TruthTable:
    """Implementation of Truth Table Entailment Method"""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.count = 0

    # return true if alpha is entailed from the knowledge base
    def __tt_entails(self, alpha):
        # creates list of symbols in kb and add symbols from alpha that are not in kb
        symbols = self.kb.symbols
        for symbol in alpha.symbols:
            if symbol not in symbols:
                symbols.append(symbol)
        return self.__tt_check_all(alpha, symbols, {})

    # enumerates through all models and checks if a model is a model of the knowledge
    # and a model of the query alpha. if model is true for both, then return true as 
    # kb entails alpha
    def __tt_check_all(self, alpha, symbols, model):
        if len(symbols) == 0: # if symbols empty, then model is complete
            all_true = True                     
            for sentence in self.kb.sentences:  # check if model is true for all sentences in kb
                if not sentence.solve(model):   
                    all_true = False                                    
            if all_true:                        # if kb is true
                alpha_solution = alpha.solve(model)
                if alpha_solution:
                    self.count+=1               # counts number of models where kb entails alpha
                return alpha_solution           # if knowledge base is true for model return solution to alpha query
            else:
                return True                     # if knowledge base is false, model doesnt matter for alpha, therefore return true 
        else:
            p = symbols[0]          # get first propositional symbol in symbol list
            rest = symbols[1:]      # get remainder of symbols
            model1 = model.copy()
            model1.update({p:True}) # add symbol to model where symbol is true
            model2 = model.copy()
            model2.update({p:False})# add symbol to model where symbol is false
            # recursively calls self until symbols is empty and a complete model can be made for kb and alpha
            return (self.__tt_check_all(alpha, rest, model1) and 
                    self.__tt_check_all(alpha, rest, model2))

    # used solve kb entails query with truth table entailment and return a string solution to print
    def solve(self, ask):
        alpha = Sentence(ask)   # convert query string to general sentence
        solution_found = self.__tt_entails(alpha)
       
        solution = "YES: " + str(self.count) if solution_found else "NO"

        return solution
