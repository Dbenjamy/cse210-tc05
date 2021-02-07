class Logic():
    """This Class calculates whether the users guess is in the word or not.

    Attributes:
        Self.numMistake tracks the total number of mistakes throughout the game
        self.letterLocation is a list of the locations of a letter in the word

    Methods:
        self.findLetter(word, guess):
            This method counts the number of times a letter appears in a word
            and tracks the number of incorrect guesses made by the user.
        self.reset
            This will reset the attribute self.letterLocation
            I put this in it's own method so that letterLocation wouldn't reset
            to empty before logic gets it. Calling it from Director at the end
            of the game loop could be a good idea.
    """

    def __init__(self):
        """Constructor and initializer

        Args:
            self: an instance of Logic()
        """
        self.numMistake = 0 # stores the number of mistakes
        self.letterLocation = [] # list for locations of a letter

    def findLetter(self, guess, word):
        """This method will compare the users guess and the word and track how
        many incorrect guesses the user has made.

        Args:
            self: an instance of Logic()
            guess: the users guess
            word: the word selected from the file
        """
        countTimes = 0 # used to count the number of times the letter appears
        newString = []
        for i in range(len(word)): # loop through the word
            if word[i] == guess: # check if any of the letters match the guess
                countTimes += 1
                newString.append(i) # add the location to the list
        if countTimes == 0: # if the letters never matched, it was a bad guess
            self.numMistake += 1
        self.letterLocation = newString
        print(self.letterLocation)
        

# to be removed as the program is completed.
word = "horse"
guess = "a"     
run = Logic()
run.findLetter(guess, word)

