def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_chars_dict(text)
    chars_list = chars_dict_to_list(letters_dict)

    #formatting print to match instructions
    print(f"--- Begin report of {book_path} ---")
    print()
    print(f"{num_words} words found in the document")
    print()

    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print()
    print("--- End report ---")


# getting the number of words in text
def get_num_words(text):
    words = text.split()
    return len(words)

# key for sorting dictionary - had to look this up 
def sort_on(d):
    return d["num"]

# converting into sorted list
def chars_dict_to_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()