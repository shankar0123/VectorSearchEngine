"""
Vector Search Engine: Step 1 - Concordance Function
This function converts a document into a word frequency dictionary.
"""

def create_concordance(document):
    """
    Converts a document (string) into a word frequency dictionary.
    
    :param document: str - The input text document.
    :return: dict - Dictionary where keys are words and values are their frequencies.
    """
    if not isinstance(document, str):
        raise ValueError("Input must be a string")

    concordance = {}  # Dictionary to store word counts
    words = document.lower().split()  # Convert to lowercase and split words

    for word in words:
        concordance[word] = concordance.get(word, 0) + 1  # Increment word count

    return concordance

# Example usage:
if __name__ == "__main__":
    sample_text = "this is a test document. this document is a sample."
    print(create_concordance(sample_text))