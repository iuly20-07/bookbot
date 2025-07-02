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
    from stats import num_words 
    print("--- Begin report of books/frankenstein.txt ---")
    num_words(file_contents)   
    print()
    letter_report(file_contents)
    print("--- End report ---")
main()