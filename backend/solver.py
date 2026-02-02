from collections import defaultdict, Counter
from typing import List

class AnagramSolver:
    def __init__(self, dictionary_path: str):
        self.dictionary_path = dictionary_path
        self.anagram_map = defaultdict(list)
        self._load_dictionary()

    def _load_dictionary(self):
        try:
            with open(self.dictionary_path, 'r') as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        sorted_word = "".join(sorted(word))
                        self.anagram_map[sorted_word].append(word)
        except FileNotFoundError:
            print(f"Error: Dictionary file not found at {self.dictionary_path}")

    def solve(self, letters: str) -> List[str]:
        """
        Finds all words that can be formed using any combination 
        of the provided letters (sub-anagrams and exact matches).
        """
        input_counts = Counter(letters.lower().replace(" ", ""))
        results = []

        for sorted_key, words in self.anagram_map.items():
            word_counts = Counter(sorted_key)

            if not (word_counts - input_counts):
                results.extend(words)

        return sorted(results, key=len, reverse=True)
