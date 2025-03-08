import math

# Step 1: Concordance Function
def create_concordance(document):
    """
    Converts a document (string) into a word frequency dictionary.
    """
    if not isinstance(document, str):
        raise ValueError("Input must be a string")

    concordance = {}
    words = document.lower().split()

    for word in words:
        concordance[word] = concordance.get(word, 0) + 1

    return concordance

# Step 2: Vector Space Model
class VectorCompare:
    def magnitude(self, concordance):
        """
        Computes the magnitude (length) of a word frequency vector.
        """
        if not isinstance(concordance, dict):
            raise ValueError("Input must be a dictionary")

        total = sum(count ** 2 for count in concordance.values())
        return math.sqrt(total)

    def similarity(self, concordance1, concordance2):
        """
        Computes cosine similarity between two word frequency vectors.
        """
        if not isinstance(concordance1, dict) or not isinstance(concordance2, dict):
            raise ValueError("Inputs must be dictionaries")

        dot_product = sum(concordance1.get(word, 0) * concordance2.get(word, 0) for word in concordance1)
        magnitude_product = self.magnitude(concordance1) * self.magnitude(concordance2)

        return dot_product / magnitude_product if magnitude_product else 0

# Step 3: Indexing Documents
documents = {
    0: "The quick brown fox jumps over the lazy dog",
    1: "The fast fox leaps over a sleeping dog",
    2: "Dogs are common pets in many households",
    3: "A fox is a wild animal, not a pet"
}

# Create a dictionary storing word frequency vectors for each document
index = {doc_id: create_concordance(text.lower()) for doc_id, text in documents.items()}

# Step 4: Search Function
def search(query):
    """
    Finds the most relevant documents based on cosine similarity.
    """
    v = VectorCompare()  # ✅ Fix: Initialize VectorCompare object
    query_vector = create_concordance(query.lower())

    matches = [(v.similarity(query_vector, index[doc_id]), doc_id) for doc_id in index]
    
    # Sort results in descending order of relevance
    matches = sorted(matches, reverse=True, key=lambda x: x[0])
    
    return matches

# Step 5: Run Search
if __name__ == "__main__":
    query = input("Enter search term: ")
    results = search(query)

    print("\nTop Matching Documents:")
    for score, doc_id in results:
        if score > 0:
            print(f"Relevance: {score:.3f} - Document {doc_id}: {documents[doc_id]}")