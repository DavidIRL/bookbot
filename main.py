def get_book_contents(path):
    with open(path) as f:
        return f.read()

def word_count(content):
    words = content.split()

    return len(words)


def main():
    book_path = "books/frankenstein.txt"
    content = get_book_contents(book_path)
    count = word_count(content)
    print(count)


main()
