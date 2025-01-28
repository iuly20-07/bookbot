def count_letters(text):
    from library import characters
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
    return characters
        

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print (count_letters(file_contents))

main()