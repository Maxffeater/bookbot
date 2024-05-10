def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    listed_char = get_listed_dict(char_dict)
    listed_char.sort(reverse=True, key=sort_on)
    build_report(book_path, num_words,listed_char)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = len(text.split())
    return words

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_listed_dict(dict):
    list = []
    for i in dict:
        list.append({"char":i,"num":dict[i]})
    return list

def sort_on(dict):
    return dict["num"]

def build_report(path, words, list):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    for dict in list:
        if dict["char"].isalpha():
            print(f"The '{dict["char"]}' character was found {dict["num"]} times")
    print("--- End report ---")


main()