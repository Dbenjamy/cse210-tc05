
class Console():
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
    
    def __init__(self):
        
        self.guess = 'z'
        self.underscores = ""


    def askDifficulty(self):

        level = input('What level of difficulty would you like? Easy (E), Medium (M), or Hard (H): ')
        if level == 'e' or level == "E":
            return 1
        elif level == 'm' or level == "M":
            return 2
        elif level == 'h' or level == "H":
            return 3
        else:
            print("Try again.")
            self.askDifficulty()

    def askForGuess(self):

        # Updates guess to whatever the user has guessed
        theirInput = input('Guess a letter [a-z]: ')
        if theirInput.isalpha() and len(theirInput) == 1:
            self.guess = theirInput.lower()
        else:
            print("Try again.")
            self.askForGuess()


    def underscoresMaker(self, word_length):

        i = 0
        while i < word_length:
            self.underscores += "_"
            i += 1
        
        


    def update_string(self, theLetter, letter_locations):
        #recieves theLetter and letter_locations from director
        i = 0
        workingString = self.underscores
        while i < len(letter_locations):
            RR = letter_locations[i]
            stringList = list(workingString)
            stringList[RR] = theLetter
            workingString = "".join(stringList)
            i += 1
        self.underscores = workingString

    def picture(self, mistakes):

        #recieves number of mistakes from logic
        #and outputs current game scenario
        pic_dict ={0:'  ___',
        1:' /___\\',
        2:' \   /',
        3:'  \ / ',
        4:'   0  ',   
        5:'  /|\ ',
        6:'  / \ '}

        new_mistake = mistakes
        while new_mistake < 7:

            if mistakes == 4:
                pic_dict[4] = '   x'

            print(pic_dict[new_mistake])
            new_mistake += 1