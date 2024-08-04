#Word Counter
def word_counter():
    print("Welcome to the Word Counter!")
    text = input("Enter the text: ")

    word_count = len(text.split())
    print(f"The text contains {word_count} words")

if __name__ == "__main__":
    word_counter()
