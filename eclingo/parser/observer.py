class WFMObserver:

    def __init__(self):
        self._facts = set()
        self._found_atoms = set()
        self._found_heads = set()

    def get_facts(self):
        return self._facts

    def reset_facts(self):
        self._facts = set()

    def get_irrelevants(self):
        return {atom for atom in self._found_atoms if atom not in self._found_heads}

    def reset_irrelevants(self):
        self._found_atoms = set()
        self._found_heads = set()

    def rule(self, choice, head, body):
        for atom in head:
            self._found_heads.add(atom)
            self._found_atoms.add(atom)
        for atom in body:
            self._found_atoms.add(atom)
        if (len(head) == 1) and not body and not choice:
            self._facts.add(head[0])
