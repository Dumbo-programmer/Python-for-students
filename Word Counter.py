import string
from collections import Counter
import os

def clean_text(text):
    # Remove punctuation
    return text.translate(str.maketrans('', '', string.punctuation))

def word_counter():
    print("Welcome to the Word Counter!")
    
    source = input("Do you want to input text directly or from a file? (type 'direct' or 'file'): ").strip().lower()

    if source == 'direct':
        text = input("Enter the text: ")
    elif source == 'file':
        file_path = input("Enter the file path: ").strip()
        if not os.path.isfile(file_path):
            print("File not found.")
            return
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        print("Invalid choice. Please type 'direct' or 'file'.")
        return
    
    # Clean and process text
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    # Calculate word count and frequency
    word_count = len(words)
    unique_words = len(set(words))
    word_freq = Counter(words)
    
    # Display results
    print(f"\nText Statistics:")
    print(f"Total number of characters (excluding spaces): {len(cleaned_text)}")
    print(f"Total number of words: {word_count}")
    print(f"Number of unique words: {unique_words}")
    
    print("\nWord Frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    word_counter()
