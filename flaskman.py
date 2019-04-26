import random
old_letters_guessed = []
num_of_tries = 0 
    num_of_tries = 0
    secret_word_random_choice()



'Casey','cast','chose','claws','coach','constantly','contrast','cookies','customs','damage','Danny','deeply','depth',\
'discussion','doll','donkey','Egypt','Ellen','essential','exchange','exist','explanation','facing','film','finest',\
'fireplace','floating','folks','fort','garage','grabbed','grandmother','habit','happily','Harry','heading','hunter'\
,'Illinois','image','independent','instant','January','kids','label','Lee','lungs','manufacturing','Martin','mathematics'\
,'melted','memory','mill','mission','monkey','Mount','mysterious','neighborhood','Norway','nuts','occasionally','official'\
,'ourselves','palace','Pennsylvania','Philadelphia','plates','poetry','policeman','positive','possibly','practical','pride',\
'promised','recall','relationship','remarkable','require','rhyme','rocky','rubbed','rush','sale','satellites','satisfied',\
'scared','selection','shake','shaking','shallow','shout','silly','simplest','slight','slip','slope','soap','solar','species'\
,'spin','stiff','swung','tales','thumb','tobacco','toy','trap','treated','tune','University','vapor','vessels','wealth','wolf','zoo']    

    """This is a dictionary for printing out hangman pictures according to user progression and failed guesses
    :param: num_of_tries: this parameter reflects how many attemps the user has already failed
    :type num_of_tries: int
    :return: HANGMAN_PHOTOS - as user declines in number of tries, prints out progressively complete hanged man
    :rtype: dict value"""
    

    elif num_of_tries == 1:
        return render_template("picture1.html")
    elif num_of_tries == 2:
        return render_template("picture2.html")
        return render_template("picture3.html")
    elif num_of_tries == 4:
        return render_template("picture4.html")
    elif num_of_tries == 5:
        return render_template("picture5.html")
    elif num_of_tries == 6:
        return render_template("picture6.html")
    elif num_of_tries == 7:
        return render_template("picture7.html")
    """This function is used to print out the secret letters not yet guessed marked with a '_' 
    :param old_guessed_letters: appends letters already guessed by user, first empty
    :type secret_word: str
    :type old_guessed_letters: list
    :return modified_word: secret word, replaced with '_' times length of word, else appenede by correct user guesses
    :rtype modified_word: list, in func return joined as str"""    
    #global secret_word    
    
    for letter in secret_word:
        if letter in old_letters_guessed:  
            modified_word.append(letter)
        else: 
            modified_word.append(' _ ')
def mainmenu():
    return render_template('mainmenu.html')
def credits():
    return render_template('credits.html')
def maingame():
    return  '<br><br>Your number of mistakes is: ' + str(num_of_tries) + '<br><br>'\
            + print_hangman(num_of_tries)\
            + show_hidden_word(secret_word, old_letters_guessed)\
            + render_template('letterguess.html')
    
    global num_of_tries
    
    letterguess = letterguess.lower()
    
    
            + '<br><br>Your number of mistakes is: ' + str(num_of_tries) + '<br><br>'\
if __name__ == "__main__":
    app.run(debug = True)