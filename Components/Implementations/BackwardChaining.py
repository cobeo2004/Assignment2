# from Components.Decorator.Export import export
# from Components.Interfaces.IBackwardChaining import IBackwardChaining
# from Components.Interfaces.IHornForm import IHornForm

# @export
# class BackwardChaining(IBackwardChaining):
#     def __init__(self, knowledgeBase: IHornForm) -> None:
#         super().__init__(knowledgeBase)
#         self.knowledgeBase = knowledgeBase

#     def __backward_chaining(self, query):
#         pass

#     def entails(self, query):
#         pass

#     def evaluate(self, query):
#         solution_found, chain = self.__bc_entails(query)

#         if solution_found:
#             # If a solution is found
#             solution = "YES: " + ", ".join(chain)
#         else:
#             # If no solution is found
#             solution = "NO"

#         return solution

# from Components.Decorator.Export import export
# from Components.Interfaces.IBackwardChaining import IBackwardChaining
# from Components.Interfaces.IHornForm import IHornForm


# @export
# class BackwardChaining(IBackwardChaining):
#     def __init__(self, knowledgeBase: IHornForm) -> None:
#         super().__init__(knowledgeBase)
#         self.inferred = set()  # To keep track of already inferred symbols
#         self.chain = []  # To keep the chain of inferences

#     def __backward_chaining(self, query):
#         # If the query is already inferred, return True
#         if query in self.inferred:
#             return True

#         # Mark the query as inferred
#         self.inferred.add(query)

#         # Check if the query is a fact
#         for sentence in self.knowledgeBase.sentences:
#             if sentence.head == query and len(sentence.conjuncts) == 0:
#                 self.chain.append(query)
#                 return True

#         # Otherwise, try to infer the query from the rules
#         for sentence in self.knowledgeBase.sentences:
#             if sentence.head == query:
#                 # Recursively check if all conjuncts can be inferred
#                 all_conjuncts_inferred = True
#                 for conjunct in sentence.conjuncts:
#                     if not self.__backward_chaining(conjunct):
#                         all_conjuncts_inferred = False
#                         break

#                 # If all conjuncts are inferred, then the query is inferred
#                 if all_conjuncts_inferred:
#                     self.chain.append(query)
#                     return True

#         # If the query cannot be inferred, return False
#         return False

#     def entails(self, query):
#         self.inferred.clear()
#         self.chain.clear()
#         isFound = self.__backward_chaining(query)
#         if isFound:
#             result = "YES: " + ", ".join(reversed(self.chain))
#         else:
#             result = "NO"
#         return result

from Components.Decorator.Export import export
from Components.Interfaces.IBackwardChaining import IBackwardChaining
from Components.Interfaces.IHornForm import IHornForm


@export
class BackwardChaining(IBackwardChaining):
    def __init__(self, knowledgeBase: IHornForm) -> None:
        super().__init__(knowledgeBase)
        self.knowledgeBase = knowledgeBase
        self.inferred = set()  # To keep track of already inferred symbols
        self.chain = []  # To keep the chain of inferences

    def __backward_chaining(self, query):
        # If the query is already inferred, return True
        if query in self.inferred:
            return True

        # Check if the query is a fact
        for sentence in self.knowledgeBase.sentences:
            if sentence.head == query and len(sentence.conjuncts) == 0:
                self.chain.append(query)
                self.inferred.add(query)
                return True

        # Otherwise, try to infer the query from the rules
        for sentence in self.knowledgeBase.sentences:
            if sentence.head == query:
                # Recursively check if all conjuncts can be inferred
                all_conjuncts_inferred = True
                for conjunct in sentence.conjuncts:
                    if not self.__backward_chaining(conjunct):
                        all_conjuncts_inferred = False
                        break

                # If all conjuncts are inferred, then the query is inferred
                if all_conjuncts_inferred:
                    self.chain.append(query)
                    self.inferred.add(query)
                    return True

        # If the query cannot be inferred, return False
        return False

    def entails(self, query):
        self.inferred.clear()
        self.chain.clear()
        isFound = self.__backward_chaining(query)
        if isFound:
            result = "YES: " + ", ".join(self.chain)
        else:
            result = "NO"
        return result
