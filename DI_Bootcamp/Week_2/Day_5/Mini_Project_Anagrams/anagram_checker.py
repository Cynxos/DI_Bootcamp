class AnagramChecker:
    def __init__(self, word_list_file):
        self.words = self.load_words(word_list_file)

    def load_words(self, file_path):
        with open(file_path, 'r') as file:
            words = file.read().split()
        return set(words)

    def is_valid_word(self, word):
        return word in self.words

    def get_anagrams(self, word):
        return [w for w in self.words if self.is_anagram(word, w)]

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2) and word1 != word2