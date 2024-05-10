from KnowledgeBase import KnowledgeBase
from Sentence import Sentence

class BackwardChaining:
    """Implementation of Backward Chaining Algorithm"""
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    # recursive functon used to prove premises are true for a given goal
    def __prove(self, removed, chain, goal):

        for sentence in self.kb.sentences:      # check if goal already given in kb
            if len(sentence.conjuncts) == 0 and goal == sentence.head:
                chain.append(goal)
                return True, chain
  
        removed.append(goal)   # mark goal as visited  
        
        for sentence in self.kb.sentences:
            if goal == sentence.head:       # loop through sentences that imply the goal
                all_true = True             # check for if all subgoals are proven
                for subgoal in sentence.conjuncts:  # loop to prove each premise of current rule of goal
                    if subgoal in chain:    # check if subgoal has already been proven true
                        continue            # skip loop if established
                    if subgoal in removed:  # check if subgoal has already been visited
                        all_true = False
                        break
                    # recursively call self to prove premise
                    established, chain = self.__prove(removed, chain, subgoal)
                    # if failed to prove subgoal, goal cannot be establish with current sentence
                    if not established:
                        all_true = False
                if all_true:            # goal is proven true all premises of a rule are proven true
                    chain.append(goal)
                    return True, chain

        return False, chain

    # backward chaining algorithm to check if kb entails query
    # algorithm starts from query, and works backwards by proving premises leading to query
    # until the query can be proved
    def __bc_entails(self, goal):
        for sentence in self.kb.sentences:      # check if goal already given in kb
            if len(sentence.conjuncts) == 0 and goal == sentence.head:
                return True, [goal]
        chain = []          # list used to display path of algorithm in solution
        removed = []        # list used to track list of visited premises to prevent loops
        return self.__prove(removed, chain, goal)

    # used solve kb entails query with backward chaining and return a string solution to print
    def solve(self, query):
        solution_found, chain = self.__bc_entails(query)
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