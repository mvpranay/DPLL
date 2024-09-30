from clause import Clause

# solver that uses dpll method
class Solver:

    def __init__(self, clauses: list):
        self.clauses = clauses

        # store only the +ve version of the literals
        self.literals = []
        for clause in self.clauses:
            for literal in clause.literals:
                if abs(literal) not in self.literals:
                    self.literals.append(abs(literal))

        # to store the vertices of implication graph
        self.vertices = []
        for literal in self.literals:
            self.vertices.append(literal)
            self.vertices.append(-literal)

        # to store edges of implication graph
        self.edges = []

        # to store decisions made
        self.decisions = []

    def checkCompletion(self):
        for clause in self.clauses:
            if clause.value == False:
                return False

        return True

    # function to find parents in implication graph
    def findParents(self, vertex):
        parents = []
        for edge in self.edges:
            if edge[1] == vertex:
                parents.append(edge[0])

        return parents

    # function to find highest level ancestors of a vertex
    def findAncestors(self, vertex):
        parents = self.findParents(vertex)
        ancestors = set()

        for parent in parents:
            ancestors.add(parent)
            grandparents = self.findAncestors(parent)
            for grandparent in grandparents:
                ancestors.add(grandparent)

        return list(ancestors)

    # checks if there exists a unit clause and returns a boolean, the clause, and the literal
    def checkUnitClause(self):

        for clause in self.clauses:
            if clause.isUnitClause():
                return True, clause, clause.getUnassignedLiteral()

        return False, None, None

    # assigns unit clauses, returns if it was possible, and the decisions that led to the conflict
    def assignUnitClauses(self):
        res, clause, literal = self.checkUnitClause()

        while res:
            clause.assignValue(literal, True)

            # add edges to implication graph
            for __literal in clause.literals:
                if __literal != literal:
                    self.edges.append((__literal, literal))

            # check for conflicts
            for c in self.clauses:
                c.assignValue(literal, True)

                # conflict
                if c.value == False:
                    # need to find all decisions that led to this conflict
                    decisions = findAncestors(literal)

                    return False, decisions


            res, clause, literal = self.checkUnitClause()

        return True, []

    # add a learnt clause from the conflict
    def addLearntClause(self, decisions):
        literals = []
        for decision in decisions:
            literals.append(-decision)

        self.clauses.append(Clause(literals))

    # function to clean up the implication graph
    def 

    def solve(self):
        while not self.checkCompletion():
            res, decisions = self.assignUnitClauses()

            if not res:
                self.addLearntClause(decisions)

                # erase the edited parts of implication graph
