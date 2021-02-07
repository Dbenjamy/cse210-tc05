


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

    def first_image(self):
        x = """  
         ___  
        /___\ 
        \   /
         \ / 
          0   
         /|\  
         / \  
        """
        return print(x)


    def askDifficulty(self):

        level = input('What level of difficulty would you like? Easy (E), Medium (M), or Hard (H): ').lower
        if level == 'e':
            return 1
        elif level == 'm':
            return 2
        return 3


    def askForGuess(self):

        # pass letters in to director/logic and they decipher
        # whether the letter is a bad guess or a good guess
        # and then passes back to me in the output function
        # if it was a bad guess
        self.guess = input('Guess a letter [a-z]: ')


    def underscores(self, word_length):

        underscore_string = ""
        i = 0
        while i < word_length:
            underscore_string.append("_")
            i += 1
        
        self.underscores = underscore_string


    def update_string(self, theLetter, letter_locations):
        #recieves theLetter and letter_locations from director
        for i in letter_locations:
            self.underscores[letter_locations[i]] = theLetter

        return print(theLetter)


    def picture(self, mistakes):

        #recieves number of mistakes from logic
        #and outputs current game scenario
        pic_dict ={0:' _____',
        1:'|_____|',
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

