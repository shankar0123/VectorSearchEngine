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

    """
Vector Search Engine: Step 3 - Document Indexing
Creates an index of multiple documents as word frequency dictionaries.
"""

documents = {
    0: "The quick brown fox jumps over the lazy dog",
    1: "The fast fox leaps over a sleeping dog",
    2: "Dogs are common pets in many households",
    3: "A fox is a wild animal, not a pet"
}

# Create a dictionary storing word frequency vectors for each document
index = {doc_id: create_concordance(text.lower()) for doc_id, text in documents.items()}

# Print the indexed documents
if __name__ == "__main__":
    for doc_id, concordance in index.items():
        print(f"Document {doc_id}: {concordance}")