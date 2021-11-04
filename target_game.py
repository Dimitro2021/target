"""programm for game"""

from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alph = string.ascii_uppercase
    grid = [random.choices(alph, k=3) for i in range(3)]
    norm_grid = []
    for line in grid:
        norm_grid += line[0] + line[1] + line[2]
    print(norm_grid)
    return grid

generate_grid()


def get_words(file_name: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(file_name) as file:
        list_of_words = []
        str_lett = str(letters)
        for line in file:
            flag = True
            line = line[:-1]
            # print(len(line))
            if 3 < len(line) < 10 and line.find(letters[4]) != -1:
                print(line)
                for letter in line:
                    if str_lett.count(letter) < line.count(letter):
                        flag = False
                if flag:
                    list_of_words.append(line)
    return(list_of_words)
                # if line.count() 
        #     line = line.lower()
        #     if line[::-1].find(letters[4]) != -1:
        #         word_list = []
        #         for letter in set(line[:-1]):
        #             word_list.append((letter, line.count(letter)))
        #         list_of_words.append([line[:-1], word_list])
        # for word in list_of_words:
        #     if
        #         return list_of_words
                # list_of_words.append(line.replace('\n', ''))
    # print(list_of_words)
# print(get_words('en.txt', ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i']))

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = input()
    return words.split()

print(get_user_words())

def checker(word: str, letters: List[str]):
    if 3 < len(word) < 10 and word.find(letters[4]) != -1:
        print(word)
        for letter in word:
            if str(letter).count(letter) < word.count(letter):
                return False
        return True


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    right_words_counter = 0
    ok_but_not_words = []
    for word in user_words.split():
        if word in words_from_dict:
            right_words_counter += 1
        else:
            if checker(word, letters):
                ok_but_not_words.append(word)
    return ok_but_not_words

# print(get_pure_user_words('mama cpxm czwpe' , ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i'], get_words('en.txt', ['e', 'm', 'x', 'p', 'c', 'z', 'w', 'p', 'i'])))

def results():
    with open('result.txt', 'w') as res_fl:
        pass

if __name__ == '___main__':
    import doctest
    print(doctest.testmod())
