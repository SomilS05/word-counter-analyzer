from unicodedata import category, normalize


def clean_text(text):
    """Fold case and separate words at Unicode punctuation."""
    text = normalize("NFC", text).casefold()
    return "".join(
        " " if category(char).startswith("P") else char
        for char in text
        if char not in "'’"
    )


def analyze_words(text):
    """Counts unique words and returns a dictionary."""
    words = clean_text(text).split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    """Main execution flow."""
    user_text = input("Enter a sentence or paragraph:\n")
    word_map = analyze_words(user_text)

    total_words = sum(word_map.values())
    unique_words = len(word_map)

    print("\n--- Analysis ---")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print("Word frequencies:", word_map)


if __name__ == "__main__":
    main()
