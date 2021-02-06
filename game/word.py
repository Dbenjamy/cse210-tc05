import random

class Word():
    """ This class will have the responsibility for finding a word
    from a file that matches the length parameter set by the user.

    Methods:
    read_file:
        Loads the contents of "words.txt" into a list.
    random_num:
        Generates a random number to use in finding a word.
    get_word:
        selects a word based on the parameter set by the user. 
        Recieves the parameter from the Director class.
"""

    def __init__(self):
        """Constructor method. Initializes the necessary lists and attributes.

        Args:
            Self: an instance of Word
        """
        # this will store the word
        self.word = "test"

        # lists are for sorting the words by length for different levels of difficulty
        self.short = []
        self.medium = []
        self.long = []


    def read_file(self):
        """This method opens the file containing 10000 words and stores them in a list.
    
        Args:
            Self: an instance of Word
        """
        # File to be read from
        # I couldn't get it to work using just "words.txt"
        path = "C:/Users/tyler/Desktop/cse210/cse210-tc05/jumper/game/words.txt"
### TODO: This will need to be changed as the program is put together ###
        
        # opens the file, writes the contents to list, and closes the file
        with open(path, "r") as text:
            self.lines_list = text.read().splitlines() # each word will be at a different location (address) in the list


    def set_list(self):
        """This method sorts each word by length and stores each in one of three lists.

        Args:
            Self: an instance of Word
        """
        # gets the total number of words in the file from the number of locations [full word]
        list_len = len(self.lines_list)

        # sorts each word by the number of letters in each one
        for i in range(list_len):
            length = len(self.lines_list[i])
            if length < 5:
                self.short.append(self.lines_list[i])       # shortest
            elif length >= 5 and length < 8:
                self.medium.append(self.lines_list[i])      # middle
            elif length >= 8:
                self.long.append(self.lines_list[i])        # longest
        

    def get_word(self, difficulty):
        """This method will select one word based on the difficulty (length)
        indicated by the user

        Args:
            Self: an instance of Word
            Difficulty: an instance of Director (used to determine about how long the word will be)

        """
        # limit stores the number of words in the list. This way, the random number generator won't generate a value 
        # that is outside of the list.
        # Index is a random memory location (loaction of a word in the list)

        if difficulty == 1:         # shortest
            limit = len(self.short)
            index = random.randint(0, limit-1)
            self.word = self.short[index]
        elif difficulty == 2:       # medium
            limit = len(self.medium)
            index = random.randint(0, limit-1)
            self.word = self.medium[index]
        elif difficulty == 3:       # longest
            limit = len(self.long)
            index = random.randint(0, limit-1)
            self.word = self.long[index]


# These are for testing purposes only and should be deleted as the program is completed. 
# director = Word()
# director.read_file()
# director.set_list()
# director.get_word(3)
