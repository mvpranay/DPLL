class Clause:

    def __init__(self, literals: list = []):
        self.literals = literals
        self.valid = self.checkValid()
        self.status = "assigned" if self.valid else "unassigned"
        self.value = True if self.valid else None
        self.assignments = {}
        
        for literal in self.literals:
            self.assignments[literal] = None
        
    def checkValid(self):
        for i in range(len(self.literals) - 1):
            for j in range(i + 1, len(self.literals)):
                if self.literals[i] + self.literals[j] == 0:
                    return True
        
        return False

    def recalculateStatus(self):
        # if the clause is valid, return
        if self.valid:
            return

        all_assigned = True
        for label in self.literals:
            if self.assignments[label] == True:
                self.status = "assigned"
                self.value = True
                return
            elif self.assignments[label] == None:
                all_assigned = False

        if all_assigned:
            self.status = "assigned"
            self.value = False
        else:
            self.status = "unassigned"
            self.value = None

        return

    def assignValue(self, label: int, value: bool):
        if label in self.literals:
            self.assignments[label] = value
        if -label in self.literals:
            self.assignments[-label] = not(value)

        self.recalculateStatus()
        return

    def deassignValue(self, label: int):
        if label in self.literals:
            self.assignments[label] = None
        
        if -label in self.literals:
            self.assignments[-label] = None

        self.recalculateStatus()
        return
        
    def printClause(self):
        if self.valid:
            print(True)
            return
        
        if self.status == "assigned":
            print(self.value)
        else:
            for label in self.literals:
                if self.assignments[label] == None:
                    print(label, end=" ")

            print()
        return
    
    def getUnassignedLiteral(self):
        for literal in self.literals:
            if self.assignments[literal] == None:
                return literal
        
        return None

    def isUnitClause(self):
        unassigned_count = 0
        unassigned_literal = None
        for literal in self.literals:
            if self.assignments[literal] == None:
                unassigned_count += 1
                unassigned_literal = literal
        
        return (unassigned_count == 1), unassigned_literal

def main():
    c = Clause([1, 2, -3, 4, -6])
    c.printClause()

    c.assignValue(3, True)
    c.printClause()

    c.assignValue(6, True)
    c.printClause()

    c.assignValue(1, False)
    c.printClause()

    c.assignValue(2, True)
    c.printClause()

    c.deassignValue(3)
    c.printClause()

    c.deassignValue(2)
    c.printClause()
    return


if __name__ == "__main__":
    main()
