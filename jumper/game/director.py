from game.word import Word
from game.console import Console
from game.logic import Logic


class Director:

    """
    The Director class will facilitate the Jumper game object interactions.

    Methods:
        __init__: builder for the class.
        start_game: plays the game.
    
    Attributes:
        word: an instance of Word.
        console: an instance of Console.
        logic: an instance of Logic.
        letter_locations: the position(s) of where the guessed letter
                         occurs.
        # I do not yet know if Logic will hold an attribute like
        # letter_locations so this might be removed.
        keep_playing: boolean, used to decide when to end the game.
        total_wrongs: int, keeps track of how many bad guesses have
                      been made, may be updated by Logic. Not sure
                      yet.



    A lot of this is technically suedo code because I do not yet know the
    names of the methods or attributes for the other classes. The calls
    made to these will be updated as the code for the other classes are
    written.
    """


    def __init__(self):
        # Making an instance of each object. Ones commented out were not
        # available at the time.

        self.word = Word()
        self.console = Console()
        self.logic = Logic()

        # Game will continue unless endgame senario is reached.
        self.keep_playing = True

        # Used to check for when the user makes a bad guess.
        self.total_wrongs = 0


    def start_game(self):
        # Makes console prompt user for their desired difficulty.
        difficulty = self.console.askDifficulty()

        # Telling word the difficulty. I am assuming that I am calling the
        # method that sets the self.word.word attribute.
        self.word.get_word(difficulty)

        # Letting console know how long the word is so it can make the
        # blank line an appropriate legnth.
        self.console.underscoresMaker(len(self.word.word))
        self.console.picture(0)

        while self.keep_playing:

            self.console.askForGuess()

            # telling logic to find letter locations
            self.logic.findLetter(self.console.guess,self.word.word)

            # checking if there were any more mistakes made
            if self.total_wrongs < self.logic.numMistake:
                self.total_wrongs = self.logic.numMistake
                self.console.picture(self.total_wrongs)

                # game ends after four bad guesses
                if self.total_wrongs == 4:
                    self.keep_playing = False
            else:
                # If the letter is in the word, console will be called to
                # to put the letters where they belong.
                self.console.update_string(self.console.guess,self.logic.letterLocation)
                self.console.picture(self.total_wrongs)
                # Console would be the first to know if the word was
                # completed, consol will have an attribute
                # that knows if the user has won. Purhaps this condition
                # could be checked by searching the string for "_" and
                # setting wonTheGame to True if it cannot find a "_"
            print(self.console.underscores)
            if not ("_" in self.console.underscores):
                print("Congradulations!")
                self.keep_playing = False