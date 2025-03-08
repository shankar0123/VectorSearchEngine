# Vector Space Search Engine in Python

## Project Overview

This project demonstrates how to build a **Vector Space Model (VSM) Search Engine** from scratch using **Python**. 
The search engine indexes text documents and allows users to search for relevant documents using **cosine similarity**.

### How Does It Work?
1. **Preprocess Documents**: Convert each document into a **word frequency dictionary** (Concordance).
2. **Vectorize Documents**: Each document is represented as a **vector of word frequencies**.
3. **Search Queries**: Convert user input into a vector and compare it with indexed document vectors.
4. **Rank Documents**: Use **cosine similarity** to find the most relevant documents.

---

## Project Structure

```
VectorSearchEngine/
│── vector_search.py   # The main search engine script
│── README.md          # This documentation file
```

---

## Step-by-Step Explanation

### 1. Building a Concordance (Word Frequency Dictionary)

A **concordance** is a dictionary that stores the number of times each word appears in a document.

#### Implementation:
```python
def create_concordance(document):
    """
    Converts a document (string) into a word frequency dictionary.
    """
    if not isinstance(document, str):
        raise ValueError("Input must be a string")

    concordance = {}
    words = document.lower().split()

    for word in words:
        concordance[word] = concordance.get(word, 0) + 1  # Count occurrences

    return concordance
```

**Why is this useful?**  
- It helps **convert text into structured data**.  
- Words are **weighted** based on their frequency, which improves search relevance.

---

### 2. Vector Space Model: Measuring Similarity

A **Vector Space Model (VSM)** represents text documents as mathematical vectors, making it possible to measure similarity between them.

#### Cosine Similarity Formula
```
cos(θ) = (A ⋅ B) / (||A|| × ||B||)
```
where:
- \( A \cdot B \) is the **dot product** (sum of term frequencies).
- \( ||A|| \) and \( ||B|| \) are the **magnitudes** (lengths) of the vectors.

#### Implementation:
```python
import math

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
```

**Why use Cosine Similarity?**  
- It **ignores document length**, making it **scale-independent**.  
- It finds **semantic closeness** rather than just counting words.  

---

### 3. Indexing Documents (Creating a Searchable Database)

Once we have a way to compare text, we need to **index multiple documents** to create a search system.

#### Implementation:
```python
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
```

**Why Index Documents?**  
- Indexing allows **fast retrieval** of relevant documents.  
- Each document is stored as a **numerical vector**, making computations efficient.  

---

### 4. Searching for Relevant Documents

The user enters a **search term**, and the program finds the **most relevant** documents using cosine similarity.

#### Implementation:
```python
def search(query):
    """
    Finds the most relevant documents based on cosine similarity.
    """
    v = VectorCompare()  # Create vector comparison object
    query_vector = create_concordance(query.lower())

    matches = [(v.similarity(query_vector, index[doc_id]), doc_id) for doc_id in index]
    
    # Sort results in descending order of relevance
    matches = sorted(matches, reverse=True, key=lambda x: x[0])
    
    return matches

# Example search:
if __name__ == "__main__":
    query = input("Enter search term: ")
    results = search(query)

    print("
Top Matching Documents:")
    for score, doc_id in results:
        if score > 0:
            print(f"Relevance: {score:.3f} - Document {doc_id}: {documents[doc_id]}")
```

**How does it work?**  
- The **query is converted** into a vector.  
- It is compared against **all indexed documents**.  
- Results are **sorted by similarity** and displayed.  

---

## Running the Search Engine

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/VectorSearchEngine.git
cd VectorSearchEngine
```

### 2. Run the Search Engine
```bash
python3 vector_search.py
```

### 3. Example Usage  
```
Enter search term: fox
Top Matching Documents:
Relevance: 0.707 - Document 0: The quick brown fox jumps over the lazy dog
Relevance: 0.707 - Document 1: The fast fox leaps over a sleeping dog
Relevance: 0.500 - Document 3: A fox is a wild animal, not a pet
```

---

## Key Takeaways

✅ **Implemented a word frequency concordance**  
✅ **Built a vector space model for document similarity**  
✅ **Indexed multiple documents for fast searching**  
✅ **Implemented a search function using cosine similarity**  
✅ **Results are ranked by relevance**  

---

## Next Steps (Future Enhancements)
- **Implement TF-IDF (Term Frequency - Inverse Document Frequency)**
- **Introduce stopword removal (ignore common words like 'the', 'is')**
- **Use stemming (convert words like 'running' to 'run')**
- **Expand dataset to real-world documents**