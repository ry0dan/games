from random import randint

words = 'baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'
array = words.split()

pics = [
'''
+---+
|
|
|
===  '''
,
'''
+---+
|   o
|
|
|
===
''' 
,
'''
+---+
|   o
|   |
|
|
===


'''
,
'''
+---+
|   o
|   |\
|
|
===
'''
,
'''
+---+
|   o
|  /|\
|
|
===

'''
,
'''
+---+
|   o
|  /|\
|   
|  /
|   
===

'''
,
'''
+---+
|   o
|  /|\
|  
|  / \
|   
===
'''

]

# choosing the secret word

def getword():
    index = randint(0,(len (array))-1)
    return array[index]

# displaying results to the player

def displayresult(mletter,cletter,secret):
    print(pics[len(mletter)])

    print('missed letters are')
    for letter in mletter:
        print(letter,end=' ')
    
    blank = '_' * len(secret)
    for i in range(len(secret)):
        if secret[i] in cletter:
            blank = blank[:i] + secretWord[i] + blank[i+1:]
    print('\ncorrect letters are')
    for letter in blank:
        
        print(letter,end=' ') 
        
# asking the player to guess a char and vlidating it

def guessword(choosen_chars):
    while True:

        print('\n***********************************************************************')
        choice = input('\nchoose letter  ')

        choice = choice.lower()

        if len(choice) != 1:
            print('choose only one letter')

        if choice in choosen_chars:
            print('you have choosen this')

        if choice not in 'abcdefghijklmnopqrstuvwxyz':
            print('i said choose a letter !!!!!!!!!!!!!')

        else:
            return choice

secretWord = getword()
cletter = ''
mletter = ''

# combining the functions together 

while True:
    print('******************WELCOME*TO*HANGMAN******************************')
    displayresult(mletter,cletter,secretWord)
    
    guess = guessword(cletter+mletter)

    if guess in secretWord:

        cletter = cletter + guess
    else:

        mletter = mletter + guess
    

# checking whether the game over or the player won

    haswon = True

    for i in range(len(secretWord)):
        if secretWord[i] not in cletter:
            haswon = False
    if haswon == True:
        print('you have won !')
        break ;
    if len(mletter) == (len(pics) - 1):
        gameover = True
        print('GaMe OveR , you just lost')
        print(pics[-1])
        break;

    
