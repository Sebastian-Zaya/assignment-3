# word_frequency.py

class WordFrequency:
    """
    A class to represent a word and its frequency count.
    """

    def __init__(self, word):
        """
        Initialize the WordFrequency with the given word and a count of 1.
        """
        self.word = word
        self.count = 1

    def increment(self):
        """Increment the frequency count by 1."""
        self.count += 1

    def get_word(self):
        """Return the stored word."""
        return self.word

    def get_count(self):
        """Return the frequency count."""
        return self.count

    def __str__(self):
        """Return a string representation of the word frequency."""
        return f"{self.word}: {self.count} occurrences"
