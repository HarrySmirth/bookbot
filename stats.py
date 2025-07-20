def get_book_text (book_file_path):
    with open(book_file_path) as f:
        book_contents = f.read()
        return book_contents

def number_of_words (file_path) :
    book_text = get_book_text(file_path)
    book_words = book_text.split()
    book_words_array = []
    for word in book_words :
        book_words_array.append(word)
    word_count = len(book_words_array)
    return f"Found {word_count} total words"

def character_count (file_path) : 
    book_content = get_book_text(file_path)
    characters = {}
    for i in book_content :
        lowercase = i.lower()
        if lowercase in characters :
            characters[lowercase] += 1
        else :
            characters[lowercase] = 1
    return characters



def sort_on(items) :
    return items["num"]
def sorted_list_of_dictionaries(dictionary) :
    list = []
    for key in dictionary :
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dictionary[key]
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list