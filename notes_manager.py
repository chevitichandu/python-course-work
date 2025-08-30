import os
import re

# Sentiment word lists
positive_words = ["good", "happy", "excellent", "great", "positive", "love"]
negative_words = ["bad", "sad", "poor", "terrible", "negative", "hate"]

NOTES_DIR = "usernotes"

# Ensure notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)


def analyze_sentiment(text: str) -> str:
    """Detect sentiment of given text using regex word search."""
    pos_count = sum(len(re.findall(rf"\b{word}\b", text, re.IGNORECASE)) for word in positive_words)
    neg_count = sum(len(re.findall(rf"\b{word}\b", text, re.IGNORECASE)) for word in negative_words)

    if pos_count > neg_count:
        return f"Positive ({pos_count} positive vs {neg_count} negative words)"
    elif neg_count > pos_count:
        return f"Negative ({neg_count} negative vs {pos_count} positive words)"
    else:
        return "Neutral"


def read_notes(filename: str = None):
    """Analyze one or all notes."""
    try:
        if filename:
            filepath = os.path.join(NOTES_DIR, filename)
            with open(filepath, "r") as f:
                content = f.read()
            print(f"\n {filename} Content:\n{content}\n")
            print("Sentiment:", analyze_sentiment(content))
        else:
            for fname in os.listdir(NOTES_DIR):
                read_notes(fname)
    except FileNotFoundError:
        print(" File not found!")


def create_note():
    """Create a new note file."""
    filename = input("Enter new note filename: ").strip() + ".txt"
    filepath = os.path.join(NOTES_DIR, filename)

    if os.path.exists(filepath):
        print(" File already exists!")
        return

    content = input("Enter note content: ")
    with open(filepath, "w") as f:
        f.write(content)
    print(f" Note '{filename}' created.")


def modify_note():
    """Modify an existing note."""
    files = os.listdir(NOTES_DIR)
    if not files:
        print(" No notes found.")
        return

    print("\nAvailable Notes:")
    for i, fname in enumerate(files, start=1):
        print(f"{i}. {fname}")

    choice = int(input("Select a note number to modify: "))
    if 1 <= choice <= len(files):
        filename = files[choice - 1]
        filepath = os.path.join(NOTES_DIR, filename)

        with open(filepath, "r") as f:
            print("\nCurrent content:\n", f.read())

        new_content = input("\nEnter new content: ")
        with open(filepath, "w") as f:
            f.write(new_content)

        print(f" Note '{filename}' updated.")
    else:
        print(" Invalid choice!")


def main():
    while True:
        print("\n==== Intelligent Notes Management System ====")
        print("1. Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                mode = input("Analyze (1) Single note or (2) All notes? ")
                if mode == "1":
                    fname = input("Enter filename: ").strip()
                    read_notes(fname)
                else:
                    read_notes()
            elif choice == 2:
                create_note()
            elif choice == 3:
                modify_note()
            elif choice == 4:
                print("👋 Exiting... Goodbye!")
                break
            else:
                print(" Invalid choice. Try again.")
        except Exception as e:
            print(" Error:", e)


if __name__ == "__main__":
    main()
