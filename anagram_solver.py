"""This code takes a word bank and a list of word lengths and returns the sentences that fit."""

from itertools import product, permutations
from sys import argv
import enchant

OUTPUT_FILE_NAME = "anagram_solver_output.txt"

def get_all_words(letter_bank, letter_count, repeats=True, sort_results=False):
    """Get all the letter combinations that are words"""
    checker = enchant.Dict("en_US")
    guesses = []
    if repeats:
        combinations = product(letter_bank, repeat=letter_count)
    else:
        combinations = permutations(letter_bank,letter_count)
    for guess in combinations:
        guess = ''.join(guess)
        if checker.check(guess):
            guesses.append(guess)
        if sort_results:
            guesses.sort()
    return guesses


def make_sentences(guesses, n=0):
    """Put the guesses together into sentences."""
    for word in guesses[n]:
        if n == len(guesses)-1:
            yield word
        else:
            for next_word in make_sentences(guesses, n+1):
                yield word + " " + next_word


def get_sentences(guesses):
    """Get All Sentences"""
    sentences = []
    for sentence in make_sentences(guesses):
        sentences.append(sentence)
    return sentences


def get_all_word_sets(letter_bank, letter_counts, repeats=True,
                      sort_results=False, sentences_not_words=False):
    """Get all the word options for each word"""
    guesses = []
    for letter_count in letter_counts:
        guesses.append(get_all_words(letter_bank, letter_count, repeats, sort_results))
    if sentences_not_words:
        return_value = get_sentences(guesses)
    else:
        return_value = []
        for guess in guesses:
            return_value.extend(guess)
    return return_value


def get_and_return_valid_combinations(letter_bank, letter_counts, repeats=True,
                                      sort_results=False, sentences_not_words=True):
    """Wrapper that gets all the sentences yields the sentences"""
    guesses = get_all_word_sets(letter_bank, letter_counts, repeats,
                                sort_results, sentences_not_words)
    sentences = []
    for sentence in make_sentences(guesses):
        sentences.append(sentence)
    return sentences


def print_sentences(letter_bank, letter_counts, sort_results=False,
                    repeats=True, sentences_not_words=True):
    """Wrapper for get_and_return_valid_combinations that prints"""
    generator = get_all_word_sets(letter_bank, letter_counts, repeats,
                                  sort_results, sentences_not_words=sentences_not_words)
    for sentence in generator:
        print(sentence)


def file_sentences(letter_bank, letter_counts, sentences_not_words=True,
                   sort_results=False, repeats=True):
    """Wrapper for get_and_return_valid_combinations that puts them in a file"""
    out_file = open(OUTPUT_FILE_NAME, 'w', encoding="utf-8")
    generator = get_all_word_sets(letter_bank, letter_counts, repeats,
                                  sort_results, sentences_not_words=sentences_not_words)
    for sentence in generator:
        out_file.write(sentence + "\n")
    out_file.close()


if __name__ == "__main__":
    if len(argv) > 3:
        FLAGS = argv[1]
        REPEATS = "r" in FLAGS
        SORT_RESULTS = "s" in FLAGS
        SENTENCES_NOT_WORDS = "w" not in FLAGS
        if "f" in FLAGS:
            FUNCTION_TO_USE = file_sentences
        else:
            FUNCTION_TO_USE = print_sentences
        LETTER_BANK = argv[2]
        argv.pop(0)
        argv.pop(0)
        argv.pop(0)
        # Cast each item in the list to an int
        argv = [int(arg) for arg in argv]
        LETTER_COUNTS = argv
        FUNCTION_TO_USE(LETTER_BANK, LETTER_COUNTS, sort_results=SORT_RESULTS, repeats=REPEATS,
                        sentences_not_words=SENTENCES_NOT_WORDS)
    else:
        print(f"""Flags:
  [f]ile output rather than print (into {OUTPUT_FILE_NAME})
  [r]epeat
  [s]ort
  [w]ords rather than senences
{argv[0]} [flags] [word bank] [word length]*
eg {argv[0]} pr zo 3 3""")