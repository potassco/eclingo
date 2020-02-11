class FactsObserver:
    def __init__(self):
        self.facts = set()
        self.found_atoms = set()
        self.found_heads = set()

    def get_facts(self):
        return self.facts

    def reset_facts(self):
        self.facts = set()

    def get_irrelevants(self):
        return {atom for atom in self.found_atoms if atom not in self.found_heads}

    def reset_irrelevants(self):
        self.found_atoms = set()
        self.found_heads = set()

    def rule(self, choice, head, body):
        for atom in head:
            self.found_heads.add(atom)
            self.found_atoms.add(atom)
        for atom in body:
            self.found_atoms.add(atom)
        if (len(head) == 1) and not body and not choice:
            self.facts.add(head[0])
