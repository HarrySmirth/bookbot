from stats import number_of_words, character_count, sorted_list_of_dictionaries,sort_on
import sys
if len(sys.argv) <2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_book = sys.argv[1]

def main():
    word_count_message = number_of_words(path_to_book)
    character_count_dictionary = character_count(path_to_book)
    sorted_dict_list = sorted_list_of_dictionaries(character_count_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(word_count_message)
    print("--------- Character Count -------")
    for i in sorted_dict_list :
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()

