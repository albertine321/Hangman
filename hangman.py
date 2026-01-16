
#Velger ord og et gyldig ord:

import random #random → brukes for å velge et tilfeldig ord.
from words import words #from words import words → henter listen words fra en annen fil (words.py).
import string #string → gir tilgang til alfabetet (string.ascii_uppercase = "A"–"Z").
word = random.choice(words).upper() #velger et tilfeldig ord fra listen og gjør det til store bokstaver.


#Hangman-figuren  

#De forskjellige stadiene (8 stadier) av hangman-figuren lagres i en liste.
hangmanfigur = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O]  |
      |
      |
      |
=========''','''
  +---+
  |   |
 [O]  |
      |
      |
      |
=========''', '''
  +---+
  |   |
 [O]  |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
 [O]  |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
 [O]  |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
 [O]  |
 /|\  |
  |   |
      |
=========''', '''
  +---+
  |   |
 [O]  |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''']

def get_valid_word(words): #sørger for at jeg får et gyldig ord uten bindestreker eller mellomrom. (trenger egt ikke funksjonen)
    word = random.choice(words) #velger et tilfeldig ord
    while'-' in word or ' ' in word: #sjekker om det er bindestrek eller mellomrom i ordet. 
        word = random.choice(words) #hvis det er bindestrek eller mellomrom, velger den et nytt ord.
        
    return word #returnerer det gyldige ordet slik at det kommer opp på hangman.

 
#Hovedfunksjonen for spillet:

def hangman(): #funksjonen for spillet.
    word = get_valid_word(words) #henter et gyldig ord. word → ordet du skal gjette.
    word_letters = set(word) #alle bokstavene som er i ordet. set gjør at det ikke er noen duplikater i ordet () → lager en mengde av unike bokstaver i ordet.
    alphabet = set(string.ascii_uppercase + "ÆØÅ") #alle bokstavene i alfabetet.
    used_letters = set() #used_letters → bokstavene du allerede har prøvd. hvis brukeren for eksempel gjetter 'A', legges 'A' til i denne mengden, A kan ikke legges inn på nytt fordi set filtrerer ut duplikater. 

    lives = len(hangmanfigur) - 1  #antall liv man har (8) basert på hvor mange hangmanfigurer.

    print("Velkommen til Hangman! ❤️") #en velkomstmelding til spilleren.

    while len(word_letters) > 0 and lives > 0: #så lenge det finnes bokstaver du ikke har gjettet ennå, og du fortsatt har liv igjen,fortsetter spillet å kjøre. bruker while-loop sånn at du kan gjette så mange bokstaver du kan så lenge du fortsatt har liv eller du ikke har gjetta ordet.
        print('Du har', lives, 'liv igjen') #viser hvor mange liv du har igjen.
        print('Disse bokstavene har du brukt før: ', ' '.join(used_letters)) #viser hvilke bokstaver du har prøvd før.

  
        print(hangmanfigur[len(hangmanfigur) - 1 - lives])  #viser den nåværende hangman-figuren basert på hvor mange liv man har igjen.

        word_list = [letter if letter in used_letters else '-' for letter in word] #lager en liste som viser de bokstavene du har gjettet riktig, og '-' for de du ikke har gjettet ennå.
        print('Nåværende ord: ', ' '.join(word_list)) #viser den nåværende tilstanden til ordet med riktige bokstaver og '-'.

        user_letter = input('Gjett en bokstav: ').upper() #tar inn en bokstav fra brukeren, og gjør den om til store bokstaver.
        print('------------------------------------------------')
        if user_letter in alphabet - used_letters: #sjekker om bokstaven er i alfabetet og ikke har blitt brukt før.
            used_letters.add(user_letter) #legger til bokstaven i used_letters.
            if user_letter in word_letters: #sjekker om bokstaven er i ordet.
                word_letters.remove(user_letter) #fjerner bokstaven fra word_letters hvis den er der.
    
            
            else:
                lives = lives - 1 #tar bort et liv hvis du tar feil
                print('Bokstaven du gjettet er ikke i ordet.')

        elif user_letter in used_letters: #hvis bokstaven er brukt før:
            print('Denne bokstaven har du prøvd før')
        
        else: #hvis det ikke er en gyldig bokstav (for eksempel tall eller tegn):
            print('Ugyldig bokstav, prøv igjen')


#Når spillet er over:

    print('------------------------------------------------')
    if lives == 0: #hvis du har mistet alle livene dine:
        print(f'Taper du klarte ikke gjette ordet som var {word} 💀')
        print(hangmanfigur[-1])  #viser den fullførte hangman-figuren når du taper.
    else: #hvis du har gjettet alle bokstavene i ordet:
        print(f'Gratulerer! Du gjettet ordet {word} 🎉')


#Starter spillet og spør om du vil spille igjen:

while True: #while True: gjør at koden kjører for alltid — til du break-er ut.
    again = input("\nTrykk ENTER for å spille, eller skriv 'Q' for å avslutte: ").strip().upper()
    if again == 'Q':
        print("Takk for at du spilte! 👋")
        break
    else:
        hangman()


"""| Del                 | Hva den gjør                                 |
   | ------------------- | -------------------------------------------- |
   | get_valid_word()    | Henter et tilfeldig gyldig ord               |
   | hangman()           | Kjører én runde av spillet                   |
   | word_letters        | Bokstaver som gjenstår å gjette              |
   | used_letters        | Bokstaver du allerede har prøvd              |
   | lives               | Antall liv igjen                             |
   | while True: nederst | Lar deg spille igjen uten å lukke programmet |
"""