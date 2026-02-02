from collections import Counter
from typing import List, Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word: Optional[str] = None

class AnagramSolver:
    def __init__(self, dictionary_path: str):
        self.dictionary_path = dictionary_path
        self.root = TrieNode()
        self._load_dictionary()

    def _load_dictionary(self):
        try:
            with open(self.dictionary_path, 'r') as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        self._insert(word)
        except FileNotFoundError:
            print(f"Error: Dictionary file not found at {self.dictionary_path}")

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def solve(self, letters: str) -> List[str]:
        """
        Finds all words that can be formed using any combination 
        of the provided letters (sub-anagrams and exact matches) using a Trie.
        """
        input_counts = Counter(letters.lower().replace(" ", ""))
        results = set()
        
        self._find_anagrams(self.root, input_counts, results)
        
        return sorted(list(results), key=len, reverse=True)

    def _find_anagrams(self, node: TrieNode, available_counts: Counter, results: set):
        if node.is_end_of_word:
            if node.word:
                results.add(node.word)
        
        # Try to extend the current prefix with available characters
        for char in available_counts:
            if available_counts[char] > 0 and char in node.children:
                # Choose
                available_counts[char] -= 1
                # Explore
                self._find_anagrams(node.children[char], available_counts, results)
                # Unchoose (Backtrack)
                available_counts[char] += 1
