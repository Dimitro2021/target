"""programm for game"""

from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alph = string.ascii_lowercase
    grid = [random.choices(alph, k=3) for i in range(3)]
    norm_grid = []
    for line in grid:
        norm_grid += line[0] + line[1] + line[2]
    print(norm_grid)
    return grid

print(generate_grid())


def get_words(file_name: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(file_name) as file:
        list_of_words = []
        str_lett = str(letters).lower()
        for line in file:
            flag = True
            line = line[:-1].lower()
            if 3 < len(line) < 10 and line.find(letters[4].lower()) != -1:
                # print('nisi budala')
                for letter in line:
                    if str_lett.count(letter) < line.count(letter):
                        flag = False
                if flag:
                    list_of_words.append(line)
                    # print('nisi budala')
    return list_of_words
# words_dict = get_words('en.txt', generate_grid())
# print(words_dict)

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = input()
    return words.split()

# print(get_user_words())

def checker(word: str, letters: List[str]):
    """go away"""
    if 3 < len(word) < 10 and word.find(letters[4]) != -1:
        for letter in word:
            if str(letters).lower().count(letter) < word.count(letter):
                return False
        return True


def get_pure_user_words(user_words: List[str], letters: List[str], \
words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    right_words_counter = 0
    ok_but_not_words = []
    for word in user_words:
        if word in words_from_dict:
            right_words_counter += 1
        else:
            if checker(word, letters):
                ok_but_not_words.append(word)
    return ok_but_not_words

def right_words(user_words: List[str], words_from_dict: List[str]) -> List[str]:
    """go away"""
    right_words_counter = 0
    for word in user_words:
        if word in words_from_dict:
            right_words_counter += 1
    return right_words_counter


def missing_words(right_wrds: List[str], all_wrds: List[str]) -> List[str]:
    """go away"""
    new_lst = []
    for wrd in all_wrds:
        if str(right_wrds).find(wrd) != -1:
            new_lst.append(wrd)
    return new_lst

def results():
    """go away"""
    lettrs = generate_grid()
    user = get_user_words()

    words_dict = get_words('en.txt', lettrs)
    right_wrd = right_words(user, words_dict)
    pure_wrd = get_pure_user_words(user, lettrs, words_dict)
    mis = missing_words(right_wrd, words_dict)
    result = str(right_wrd) + ' ' + str(words_dict) + ' ' + str(mis) + ' ' + str(pure_wrd)
    # print('ovdje sam', right_wrd, words_dict, mis, pure_wrd)
    print(result)
    with open('result.txt', 'w') as res_fl:
        res_fl.write(result)
    return 'ewdcxz'
