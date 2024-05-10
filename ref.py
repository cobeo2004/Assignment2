class InferenceEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def check_tt(self, query):
        # Create all possible truth assignments for propositions
        import itertools
        symbols = {
            symbol for clause in self.kb for symbol in clause.replace('=>', '')}
        for values in itertools.product([False, True], repeat=len(symbols)):
            assignment = dict(zip(symbols, values))
            if all(self.evaluate(clause, assignment) for clause in self.kb):
                if assignment.get(query, False):
                    return True
        return False

    def evaluate(self, expression, assignment):
        if "=>" in expression:
            premises, conclusion = expression.split("=>")
            premises = premises.split('&')
            return not all(assignment.get(p.strip(), False) for p in premises) or assignment.get(conclusion.strip(), False)
        return assignment.get(expression.strip(), False)

    def check_bc(self, query):
        from collections import deque
        goal_stack = deque([query])
        while goal_stack:
            goal = goal_stack.pop()
            if goal not in [clause.split('=>')[-1].strip() for clause in self.kb]:
                continue
            for rule in self.kb:
                premises, conclusion = rule.split('=>')
                if conclusion.strip() == goal:
                    for premise in premises.split('&'):
                        if premise.strip() not in goal_stack:
                            goal_stack.append(premise.strip())
            if all(premise in self.kb for premise in goal_stack):
                return True
        return False

    def check_fc(self, query):
        inferred = {}
        agenda = [fact for fact in self.kb if "=>" not in fact]
        while agenda:
            p = agenda.pop()
            if p == query:
                return True
            if p not in inferred:
                inferred[p] = True
                for rule in self.kb:
                    if "=>" in rule:
                        premises, conclusion = rule.split('=>')
                        if p in premises:
                            premises = premises.split('&')
                            if all(inferred.get(prem.strip(), False) for prem in premises):
                                agenda.append(conclusion.strip())
        return False


# Example Knowledge Base and Queries
kb = ["p2", "p3", "a", "b", "p2&p1&p3 => d",
      "p1&p3 => c", "b&e => f", "f&g => h"]
engine = InferenceEngine(kb)

# Query
query = "d"

# Checking with different methods
print("Truth Table Checking:", engine.check_tt(query))
# print("Backward Chaining:", engine.check_bc(query))
print("Forward Chaining:", engine.check_fc(query))
