import numpy as np
import random
from collections import defaultdict

class MarkovText:
    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):
        term_dict = defaultdict(list)
        for i in range(len(self.corpus) - 1):
            current_token = self.corpus[i]
            next_token = self.corpus[i + 1]
            term_dict[current_token].append(next_token)
        self.term_dict = dict(term_dict)
        return None

    def generate(self, seed_term=None, term_count=15):
        if self.term_dict is None:
            self.get_term_dict()
        if not self.term_dict:
            return ""

        if seed_term is not None:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_term = seed_term
        else:
            current_term = random.choice(list(self.term_dict.keys()))

        output = [current_term]
        for _ in range(term_count - 1):
            next_terms = self.term_dict.get(current_term)
            if not next_terms:
                break
            current_term = np.random.choice(next_terms)
            output.append(current_term)

        return " ".join(output)