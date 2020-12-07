import string
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for e in secret_word:
        if e not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    mylist = []
    for i in secret_word:
        mylist.append(i)
    for i in range(len(mylist)):
        if mylist[i] not in letters_guessed:
            mylist[i] = '_ '
    return ''.join(mylist)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabets = string.ascii_lowercase
    available_letters = []
    for i in alphabets:
        if i not in letters_guessed:
            available_letters.append(i)
    return ''.join(available_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    print("-" * 20)
    guesses_left = 6
    letters_guessed = []
    warnings_left = 3
    while guesses_left:
        print("You have", guesses_left, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        user_guess = (input("Please guess a letter: ").lower())
        if user_guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        if not str.isalpha(user_guess) or len(user_guess) != 1:
            print("Oops! That is not a valid letter! Warning(s) left:", warnings_left-1)
            print("-" * 20)
            warnings_left -= 1
            if warnings_left == 0:
                print("You lose one guess.")
                guesses_left -= 1
                warnings_left = 3
            continue
        if user_guess in letters_guessed:
            print("Oops! You've already guessed that letter! Warning(s) left:", warnings_left - 1)
            print(get_guessed_word(secret_word, letters_guessed))
            print("-" * 20)
            warnings_left -= 1
            if warnings_left == 0:
                print("You lose one guess.")
                guesses_left -= 1
                warnings_left = 3
            continue
        letters_guessed.append(user_guess)
        if user_guess not in secret_word:
            print("Oops! That letter is not in my word.")
            if user_guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_left -= 1
        else:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            if get_guessed_word(secret_word, letters_guessed) == secret_word:
                print("Congratulations! You won!")
                print("Your total score for this game is:", guesses_left * len(set(secret_word)))
                return
            guesses_left += 1
        guesses_left -= 1
        print("-" * 20)
    print("Sorry! You ran out of guesses. The word was", secret_word)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == '_':
            continue
        if my_word[i] != other_word[i]:
            return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    no_match = True
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)
            no_match = False
    if no_match:
        print("No matches found.")


hangman(choose_word(wordlist))
