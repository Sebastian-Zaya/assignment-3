from QuadHash import QuadHash
from word_frequency import WordFrequency

def clean_word(raw_word):
    # Convert to lowercase
    word = raw_word.lower()

    # Remove leading non-alphabetic characters
    start = 0
    while start < len(word) and not word[start].isalpha():
        start += 1

    # Remove trailing non-alphabetic characters
    end = len(word) - 1
    while end >= start and not word[end].isalpha():
        end -= 1

    # Extract the core word
    if start > end:
        return None  # No alphabetic characters found

    word = word[start:end+1]

    # Remove internal non-alphabetic characters (e.g., hyphens, apostrophes)
    cleaned_word = ''.join(char for char in word if char.isalpha())

    if len(cleaned_word) == 0:
        return None

    return cleaned_word

def build_frequency_table(filename, interesting_words=None):
    """
    Read the file and build a hash table of WordFrequency objects.
    If 'interesting_words' is provided, it's a list of words to track specifically.
    """
    freq_table = QuadHash(initial_capacity=31)  # Start with a prime number

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # Split the line into words based on whitespace
            tokens = line.split()
            for token in tokens:
                cleaned = clean_word(token)
                if cleaned is None:
                    continue  # Skip empty or non-alphabetic tokens

                # Retrieve the existing WordFrequency object
                wf_obj = freq_table.get(cleaned)
                if wf_obj is None:
                    # If it doesn't exist, create a new one and add it to the table
                    wf_obj = WordFrequency(cleaned)
                    freq_table.add(cleaned, wf_obj)
                else:
                    # If it exists, increment its count
                    wf_obj.increment()
                    freq_table.add(cleaned, wf_obj)  # Update the table with the incremented object

    return freq_table

def main():
    # Define the Lovecraftian terms to track
    lovecraftian_terms = [
        "cthulhu",
        "azathoth",
        "kadath",
        "yuggoth",
        "nyarlathotep",
        "necronomicon"
    ]

    # Build the frequency table from the Lovecraft text
    freq_table = build_frequency_table("/Users/sebastianzayaalexandros/Documents/programming/assignments/data structures/assignment-3/lecture-9/lovecraft.txt")

    print("Here are the frequencies of classic Lovecraftian terms")
    print("------------------------------------------------------")

    for term in lovecraftian_terms:
        wf_obj = freq_table.get(term)
        if wf_obj is not None:
            print(f"{wf_obj.get_word()}: {wf_obj.get_count()} occurrences")
        else:
            print(f"{term.capitalize()}: 0 occurrences")

if __name__ == "__main__":
    main()
