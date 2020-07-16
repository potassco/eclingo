class WFMObserver:

    def __init__(self):
        self._facts = set()
        self._rules = []

    def get_facts(self):
        return self._facts

    def reset_facts(self):
        self._facts = set()

    def get_heads(self, externals):
        return {atom for head, body in self._rules for atom in head
                if not externals.intersection(body)}

    def reset_heads(self):
        self._rules = []

    def rule(self, choice, head, body):
        if (len(head) == 1) and not body and not choice:
            self._facts.add(head[0])
        self._rules.append((head, body))
