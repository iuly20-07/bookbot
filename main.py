def letter_report(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    for char, count in characters.items():
        print(f"The '{char}' character was found {count} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    letter_report(file_contents)
    print("--- End report ---")
main()