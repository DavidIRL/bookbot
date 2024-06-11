def get_book_contents(path):
    with open(path) as f:
        return f.read()


def word_count(content):
    words = content.split()
    return len(words)


def character_count(content):
    char_dict = {}
    for char in content.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def create_report(path, count, char_lst):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in document {path}\n")
    for entry in char_lst:
        if not entry["char"].isalpha():
            continue
        print(f"The {entry['char']} character occurred {entry['num']} times in {path}")
    print("--- End report ---")


def dict_sort(dict):
    char_lst = []
    for entry in dict:
        char_lst.append({"char": entry, "num": dict[entry]})
    char_lst.sort(reverse=True, key=sorter)
    return char_lst


def sorter(dict):
    return dict["num"]


def main():
    path = "books/frankenstein.txt"
    content = get_book_contents(path)
    count = word_count(content)
    characters = character_count(content)
    char_lst = dict_sort(characters)
    create_report(path, count, char_lst)


main()
