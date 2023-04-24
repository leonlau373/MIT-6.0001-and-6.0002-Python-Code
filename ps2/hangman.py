# Problem Set 2, hangman.py
# Name: Leon
# Collaborators: -
# Time spent: +- 2 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    '''
    Idea: Nothing interesting, just checking each letters in secret word has a representation
          or not in the letters_guessed list
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
      if char not in letters_guessed:
        return False

    return True

#print(is_word_guessed("apples",['a', 'l', 'e', 'p', 'r', 's']))
'''
This is fine
'''

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    '''
    Idea: Same as the is_word_guessed, scan through the secret_word and do what we want
          in our list
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_list = []
    for char in secret_word:
      if char not in letters_guessed:
        guessed_list.append('_')
      else:
        guessed_list.append(char)
    
    return ' '.join(guessed_list)

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed) )
'''
This is fine
'''


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    chars = string.ascii_lowercase
    char_list = list(chars)
    for x in letters_guessed:
      char_list.remove(x)
    chars = ''.join(char_list)
    return chars

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (get_available_letters(letters_guessed))


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
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have 3 warnings left")
    print("-------------")

    guesses = 6
    letters_guessed = []
    warning = 3
    chars = string.ascii_lowercase

    unique_secret = []
    for char in secret_word:
      if char not in unique_secret:
        unique_secret.append(char)

    while not (is_word_guessed(secret_word, letters_guessed) or guesses < 1):
      print("-------------")
      print("You have", warning, "warning(s) left")
      print("You have", guesses, "guess(es) left")
      print("Available letters:", get_available_letters(letters_guessed))
      letter = input("Please guess a letter: ")
      letter = letter.lower() #lowercase the alphabet
      
      if letter not in letters_guessed and letter.isalpha():
        letters_guessed.append(letter)
        if letter in secret_word:
          print("Good guess:", get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
          if letter in "aiueo":
            guesses = guesses - 2
          else:
            guesses = guesses - 1
      
      elif letter in letters_guessed:
        if warning > 0:
          warning = warning - 1
          print("Oops! You've already guessed that letter. You now have", warning, "warning(s):", get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! You've already guessed that letter. You have no warnings left")
          print("so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          guesses = guesses - 1
      
      elif not letter.isalpha():
        if warning > 0:
          warning = warning - 1
          print("Oops! That's not a valid letter. You now have", warning, "warning(s):")
          print(get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That's not a valid letter. You have no warnings left")
          print("so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          guesses = guesses - 1
    if is_word_guessed(secret_word,letters_guessed):
      print("-------------")
      print("Congratulations, you won!")
      print("Your total score for this game is:", guesses*len(unique_secret))
    elif guesses < 1:
      print("-------------")
      print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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
    my_word_list = my_word.split(' ')
    other_word_list = list(other_word)

    unique_letter = []
    for char in my_word_list:
      if char != "_" and char not in unique_letter:
        unique_letter.append(char)

    if len(my_word_list) == len(other_word_list):
      for x in range(len(my_word_list)):
        #When we check the _ slot
        if my_word_list[x] == "_" and other_word_list[x] in unique_letter:
          return False
        #Comparing when the slot is not _
        elif my_word_list[x] != "_" and my_word_list[x] != other_word_list[x] :
          return False
    else:
      return False

    return True

#print(match_with_gaps("a _ p l e", "ample"))



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
    possiblewords = []
    for words in wordlist:
      if match_with_gaps(my_word, words):
        possiblewords.append(words)
    
    if len(possiblewords) == 0:
      print("No matches found")
    else:
      print(' '.join(possiblewords))

#show_possible_matches("a b b b _")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have 3 warnings left")
    print("-------------")

    guesses = 6
    letters_guessed = []
    warning = 3
    chars = string.ascii_lowercase

    unique_secret = []
    for char in secret_word:
      if char not in unique_secret:
        unique_secret.append(char)

    while not (is_word_guessed(secret_word, letters_guessed) or guesses < 1):
      print("-------------")
      print("You have", warning, "warning(s) left")
      print("You have", guesses, "guess(es) left")
      print("Available letters:", get_available_letters(letters_guessed))
      letter = input("Please guess a letter: ")
      letter = letter.lower() #lowercase the alphabet
      
      if letter not in letters_guessed and letter.isalpha():
        letters_guessed.append(letter)
        if letter in secret_word:
          print("Good guess:", get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
          if letter in "aiueo":
            guesses = guesses - 2
          else:
            guesses = guesses - 1
      
      elif letter in letters_guessed:
        if warning > 0:
          warning = warning - 1
          print("Oops! You've already guessed that letter. You now have", warning, "warning(s):", get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! You've already guessed that letter. You have no warnings left")
          print("so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          guesses = guesses - 1
      
      elif not letter.isalpha():
        if letter == "*":
          print("Possible word matches are:")
          show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        elif warning > 0:
          warning = warning - 1
          print("Oops! That's not a valid letter. You now have", warning, "warning(s):")
          print(get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That's not a valid letter. You have no warnings left")
          print("so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
          guesses = guesses - 1
    if is_word_guessed(secret_word,letters_guessed):
      print("-------------")
      print("Congratulations, you won!")
      print("Your total score for this game is:", guesses*len(unique_secret))
    elif guesses < 1:
      print("-------------")
      print("Sorry, you ran out of guesses. The word was", secret_word)
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)