from Components.Decorator.Export import export
from Components.Interfaces.IBackwardChaining import IBackwardChaining


@export
class BackwardChaining(IBackwardChaining):
    def __init__(self, knowledgeBase) -> None:
        ###########
        # IBackwardChaining initializer
        # self.knowledgeBase = knowledgeBase  # The knowledge base that alogrithm will use
        # self.inferred = set()  # To keep track of already inferred symbols
        # self.chain = []  # To keep the chain of inferences
        ###########
        super().__init__(knowledgeBase)

    def __backward_chaining(self, query):
        # If the query is already inferred, return True
        if query in self.inferred:
            return True

        # Check if the query is a fact in the knowledge base
        for sentence in self.knowledgeBase.sentences:
            if sentence.head == query and len(sentence.conjuncts) == 0:
                # If the query is a fact (no conjuncts), add it to the chain and inferred set
                self.chain.append(query)
                self.inferred.add(query)
                return True

        # Otherwise, try to infer the query using the rules in the knowledge base
        for sentence in self.knowledgeBase.sentences:
            if sentence.head == query:
                # Check if all conjuncts of the rule can be inferred recursively
                all_conjuncts_inferred = True
                for conjunct in sentence.conjuncts:
                    if not self.__backward_chaining(conjunct):
                        all_conjuncts_inferred = False
                        break

                # If all conjuncts are inferred, then the query can be inferred
                if all_conjuncts_inferred:
                    self.chain.append(query)
                    self.inferred.add(query)
                    return True

        # If the query cannot be inferred from the facts or rules, return False
        return False

    def entails(self, query):
        # Clear the inferred set and chain list before starting
        self.inferred.clear()
        self.chain.clear()

        # Start the backward chaining process to determine if the query can be inferred
        isFound = self.__backward_chaining(query)

        # Format the result based on whether the query can be inferred or not
        if isFound:
            result = "YES: " + ", ".join(self.chain)
        else:
            result = "NO"

        # Return the result
        return result
