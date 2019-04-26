import random
from flask import Flask, request, render_template

app = Flask(__name__)

global old_letters_guessed
old_letters_guessed = []
global num_of_tries
num_of_tries = 0 
global secret_word

def game_reset():
    global old_letters_guessed
    global num_of_tries
    global secret_word
    old_letters_guessed = []
    num_of_tries = 0
    secret_word_random_choice()

def secret_word_random_choice():
    global secret_word
    wordslist = ['advice','arrangement','attempt','August','Autumn','border','breeze','brick','calm','canal',\
'Casey','cast','chose','claws','coach','constantly','contrast','cookies','customs','damage','Danny','deeply','depth',\
'discussion','doll','donkey','Egypt','Ellen','essential','exchange','exist','explanation','facing','film','finest',\
'fireplace','floating','folks','fort','garage','grabbed','grandmother','habit','happily','Harry','heading','hunter'\
,'Illinois','image','independent','instant','January','kids','label','Lee','lungs','manufacturing','Martin','mathematics'\
,'melted','memory','mill','mission','monkey','Mount','mysterious','neighborhood','Norway','nuts','occasionally','official'\
,'ourselves','palace','Pennsylvania','Philadelphia','plates','poetry','policeman','positive','possibly','practical','pride',\
'promised','recall','relationship','remarkable','require','rhyme','rocky','rubbed','rush','sale','satellites','satisfied',\
'scared','selection','shake','shaking','shallow','shout','silly','simplest','slight','slip','slope','soap','solar','species'\
,'spin','stiff','swung','tales','thumb','tobacco','toy','trap','treated','tune','University','vapor','vessels','wealth','wolf','zoo']    

    secret_word = random.choice(wordslist)

def print_hangman(num_of_tries):
    """This is a dictionary for printing out hangman pictures according to user progression and failed guesses
    :param: num_of_tries: this parameter reflects how many attemps the user has already failed
    :type num_of_tries: int
    :return: HANGMAN_PHOTOS - as user declines in number of tries, prints out progressively complete hanged man
    :rtype: dict value"""

    if num_of_tries == 0:
        return render_template("picture0.html")
    elif num_of_tries == 1:
        return render_template("picture1.html")
    elif num_of_tries == 2:
        return render_template("picture2.html")
    elif num_of_tries == 3:
        return render_template("picture3.html")
    elif num_of_tries == 4:
        return render_template("picture4.html")
    elif num_of_tries == 5:
        return render_template("picture5.html")
    elif num_of_tries == 6:
        return render_template("picture6.html")
    elif num_of_tries == 7:
        return render_template("picture7.html")
    
def show_hidden_word(secret_word, old_letters_guessed):
    """This function is used to print out the secret letters not yet guessed marked with a '_' 
    :param old_guessed_letters: appends letters already guessed by user, first empty
    :type secret_word: str
    :type old_guessed_letters: list
    :return modified_word: secret word, replaced with '_' times length of word, else appenede by correct user guesses
    :rtype modified_word: list, in func return joined as str"""    
    #global secret_word    
    modified_word = []
    
    for letter in secret_word:
        if letter in old_letters_guessed:  
            modified_word.append(letter)
        else: 
            modified_word.append(' _ ')
    return(str('<br><br>'+' '.join(modified_word)))

@app.route('/')
def printro():
    return render_template('printro.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/mainmenu')
def mainmenu():
    return render_template('mainmenu.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/letterguess')
def maingame():
    return  '<br><br>Your number of mistakes is: ' + str(num_of_tries) + '<br><br>'\
            + print_hangman(num_of_tries)\
            + show_hidden_word(secret_word, old_letters_guessed)\
            + render_template('letterguess.html')

@app.route('/lettercheck', methods=['POST'])
def lettercheck():
    
    global old_letters_guessed
    old_letters_guessed = sorted(old_letters_guessed)
    #oldletterstr = '<br><br> This a list of previously guessed letters:  [' + ', '.join(old_letters_guessed) + ']<br><br>'
    
    global secret_word
    global num_of_tries
    #mistakestr = '<br><br>Your number of tries is: ' + str(num_of_tries)
    
    letterguess = request.form['letterguess']
    letterguess = letterguess.lower()
    
    while num_of_tries <= 7:
    
        if letterguess not in old_letters_guessed and letterguess in secret_word:
            old_letters_guessed += letterguess
            if '_' not in show_hidden_word(secret_word, old_letters_guessed):
                game_reset()
                return render_template('win.html')
            
            else:
                return 'Good guess, you\'re on the right track!:    ' + letterguess\
                + '<br><br>This a list of previously guessed letters:  [' + ', '.join(old_letters_guessed) + ']<br><br>' \
                + '<br><br>Your number of mistakes is: ' + str(num_of_tries) + '<br><br>'\
                + print_hangman(num_of_tries)\
                + show_hidden_word(secret_word, old_letters_guessed)\
                + render_template('letterguess.html')
        
        elif letterguess not in old_letters_guessed and letterguess not in secret_word:
            num_of_tries += 1
            if num_of_tries >= 7:
                game_reset()
                return render_template('lose.html')
                
            else:
                old_letters_guessed += letterguess
                return 'This letter is not in the secret word, too bad for you!<br><br>'\
                + '<br><br>Your number of mistakes is: ' + str(num_of_tries)\
                + '<br><br> This a list of previously guessed letters:  [' + ', '.join(old_letters_guessed) + ']<br><br>' \
                + print_hangman(num_of_tries)\
                + show_hidden_word(secret_word, old_letters_guessed)\
                + render_template('letterguess.html')
    
        else: 
            return 'You have already guessed this letter, '\
            + '<br><br> This a list of previously guessed letters:  [' + ', '.join(old_letters_guessed) + ']<br><br>'\
            + '<br><br>Your number of mistakes is: ' + str(num_of_tries) + '<br><br>'\
            + print_hangman(num_of_tries)\
            + show_hidden_word(secret_word, old_letters_guessed)\
            + render_template('letterguess.html')

if __name__ == "__main__":
    secret_word_random_choice()
    app.run(debug = True)
