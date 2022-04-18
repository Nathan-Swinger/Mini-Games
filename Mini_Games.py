import random
from tabnanny import check
import tkinter

class mainMenu(object):

    def run():
        print("1. Number guessing game")
        print("2. Craps")
        print("3. BlackJack")
        print("4. Quit")
        command = input("What game would you like to play?")   
        if command == "1":
            numberGuessingGame.start()
        elif command == "2":
            craps.confirmation()
        elif command == "3":
            BlackJack.confirmation()
        elif command == "4":
            print("Program is now closing...")
        else:
            print("Invalid Entry: Try again")
            mainMenu.run()
            
class numberGuessingGame():

    def confirmation():
        start = input("Welcome to the number guessing game, would you like to play? (y/n)")
        start = start.lower()
        if start == ("y"):
            numberGuessingGame.start()
        elif start == ("n"):
            print("Returning to main menu...")
            mainMenu.run()

    def start():
            LowRange = input("Enter the lower bound of numbers you want to guess: ")
            HighRange = input("Enter the higher bound of numbers you want to guess(inclusive): ")
            number = random.randint(int(LowRange), int(HighRange))
            keepGoing = 1
            count = 0
            while keepGoing == 1:
                guess = input("Enter your guess between " + str(LowRange) + " and " + str(HighRange) + ": ")
                if int(guess) < number:
                    print("Number is higher.")
                    count += 1
                if int(guess) > number:
                    print("Number is lower.")
                    count += 1
                elif int(guess) == number:
                    count += 1
                    keepGoing = 0
            if count == 0:
                count += 1
            print("You win!")
            print("It took you " + str(count) + " guesses to win.")
            newGame = input("Would you like to play again? (y/n)")
            newGame = newGame.lower()
            if newGame == ("y"):
                numberGuessingGame.start()
            elif newGame == ("n"):
                print("Returning to main menu...")
                mainMenu.run()

class craps():

    def start():
        rollAgain = True
        while rollAgain == True:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            print(d1, d2)
            aSum = d1 + d2
            if aSum == 7 or aSum == 11:
                print("You win")
                newGame = input("Would you like to play again? (y/n)")
                newGame = newGame.lower()
                rollAgain = False
                if newGame == ("y"):
                    craps.start()
                elif newGame == ("n"):
                    print("Returning to main menu...")
                    mainMenu.run()
            elif aSum == 2 or aSum == 3 or aSum == 12:
                print("You lose")
                newGame = input("Would you like to play again? (y/n)")
                newGame = newGame.lower()
                rollAgain = False
                if newGame == ("y"):
                    craps.start()
                elif newGame == ("n"):
                    print("Returning to main menu...")
                    mainMenu.run()
                else:
                    rollAgain = True

class Cards():

    def createDeck():
        Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        Ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        Deck = []
        for x in Suits:
            for y in Ranks:
                Card = (x, y)
                Deck.append(Card)
        random.shuffle(Deck)
        return Deck

class BlackJack():

    def confirmation():
        start = input("Welcome to the game of Blackjack, would you like to play? (y/n)")
        start = start.lower()
        if start == ("y"):
            BlackJack.start()
        elif start == ("n"):
            print("Returning to main menu...") 
            mainMenu.run()

    def valueCheck(x):
        if x > 10 and x < 14:
            return 10
        elif x == 14:
            return 11
        else:
            return x
    
    def winEvaluator(x, y, pBust, dBust):
        if x == y:
            print("Push!")
        elif dBust == True:
            print("You win!")
        elif pBust == True:
            print("Dealer wins!")
        elif x > y and pBust == False:
            print("You win!")
        elif y > x and dBust == False:
            print("Dealer wins!")

    def start():

        ##########################################
        #   Generate a deck and a player Hand    #
        ##########################################
        blackJackDeck = Cards.createDeck()
        cardSelector1 = random.randint(0,51)
        playerHandValue = 0
        firstCard = blackJackDeck.pop(cardSelector1)
        firstCardValue = firstCard[1]
        playerHandValue += BlackJack.valueCheck(firstCardValue)
        cardSelector2 = random.randint(0,50)
        secondCard = blackJackDeck.pop(cardSelector2)
        secondCardValue = secondCard[1]
        playerHandValue += BlackJack.valueCheck(secondCardValue)
        playerCardsInHand = [firstCard, secondCard]
        aceChecker = [firstCard, secondCard]
        cardsLeft = 49
        keepGoing = 1
        playerBust = False
        dealerBust = False
#############################################################################
#  Start player turn loop and adjust values of face cards to proper value   #
#  (Have to adjust value since deck class generates face cards as > 10)     # 
#############################################################################

        while keepGoing == 1 and len(aceChecker) > 0:
            #############################################################################
            # If player hand value > 21 check for aces and turn their values to ones    #
            #############################################################################
            if playerHandValue > 21:
                for x in aceChecker:
                    theCardValue = x[1]
                    checkedValue = BlackJack.valueCheck(theCardValue)
                    if checkedValue == 11:
                        playerHandValue -= 10
                    aceChecker.remove(x)
            ##############################################################
            #  If player has busted, end game and output hand + values   #
            ##############################################################
            if playerHandValue > 21:
                print("Cards: ")
                for x in playerCardsInHand:
                    if x[1] == 11:
                        print("Jack of " + x[0])
                    elif x[1] == 12:
                        print("Queen of " + x[0])
                    elif x[1] == 13:
                        print("King of " + x[0])
                    elif x[1] == 14:
                        print("Ace of " + x[0])
                    else:
                        print(str(x[1]) + " of " + x[0])
                print("Value of hand: " + str(playerHandValue))
                print("Bust!")
                playerBust = True
                keepGoing = 0
                break

            #########################################################################################
            #  Print cards in players hand and their values, ask player if they would like to hit   #
            #########################################################################################

            print("Cards: ")
            for x in playerCardsInHand:
                if x[1] == 11:
                    print("Jack of " + x[0])
                elif x[1] == 12:
                    print("Queen of " + x[0])
                elif x[1] == 13:
                    print("King of " + x[0])
                elif x[1] == 14:
                    print("Ace of " + x[0])
                else:
                    print(str(x[1]) + " of " + x[0])
            print("Value of hand: " + str(playerHandValue))
            hit = input("\n Would you like to hit? (y/n)")
            hit = hit.lower()

            #############################################################################################
            #  If player wants hit, generate another card, add it to hand, adjust value and add value   #
            #############################################################################################

            if(hit == "y"):
                anotherCardSelector = random.randint(0,cardsLeft)
                anotherCard = blackJackDeck.pop(anotherCardSelector)
                anotherCardValue = anotherCard[1]
                playerHandValue += BlackJack.valueCheck(anotherCardValue)
                playerCardsInHand.append(anotherCard)
                aceChecker.append(anotherCard)
                cardsLeft -= 1
            else:
                keepGoing = 0
        
            ########################################
            #   Repeat above process for dealer    #
            ########################################

        dealerHandValue = 0
        dealerCardSelector1 = random.randint(0, cardsLeft)
        firstDealerCard = blackJackDeck.pop(dealerCardSelector1)
        firstDealerCardValue = firstDealerCard[1]
        dealerHandValue += BlackJack.valueCheck(firstDealerCardValue)
        cardsLeft -= 1
        dealerCardSelector2 = random.randint(0, cardsLeft)
        secondDealerCard = blackJackDeck.pop(dealerCardSelector2)
        secondDealerCardValue = secondDealerCard[1]
        dealerHandValue += BlackJack.valueCheck(secondDealerCardValue)
        cardsLeft -= 1
        dealerCardsInHand = [firstDealerCard, secondDealerCard]
        dealerAceChecker = [firstDealerCard, secondDealerCard]
        if dealerHandValue > 21:
            for x in dealerAceChecker:
                theDealerCardValue = x[1]
                checkedDealerValue = BlackJack.valueCheck(theDealerCardValue)
                if checkedDealerValue == 11:
                    dealerHandValue -= 10
                aceChecker.remove(x)
        if playerHandValue < 21:
            while dealerHandValue < playerHandValue:
                anotherDealerCardSelector = random.randint(0, cardsLeft)
                anotherDealerCard = blackJackDeck.pop(anotherDealerCardSelector)
                anotherDealerCardValue = anotherDealerCard[1]
                dealerHandValue += BlackJack.valueCheck(anotherDealerCardValue)
                dealerCardsInHand.append(anotherDealerCard)

        print("Dealer's Cards: ")
        for x in dealerCardsInHand:
            if x[1] == 11:
                print("Jack of " + x[0])
            elif x[1] == 12:
                print("Queen of " + x[0])
            elif x[1] == 13:
                print("King of " + x[0])
            elif x[1] == 14:
                print("Ace of " + x[0])
            else:
                print(str(x[1]) + " of " + x[0])
        print("Value of dealer's hand: " + str(dealerHandValue))

        ######################################################################
        #   Evaluate win and ask player if they would like to play again     #
        ######################################################################
        if dealerHandValue > 21:
            dealerBust = True
        winValue = BlackJack.winEvaluator(playerHandValue, dealerHandValue, playerBust, dealerBust)
        playAgain = input("\n Would you like to play again?(y/n)")
        playAgain = playAgain.lower()
        if playAgain == "y":
            BlackJack.start()
        else:
            print("Returning to main menu...")
            mainMenu.run()

def main():
    mainMenu.run()

main()
