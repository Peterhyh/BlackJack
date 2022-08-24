import random
import time


while True:
#variables
    player = True
    dealer = True

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    #storing card values here
    playerCard = []
    dealerCards = [] 

#functions:
    #generating random cards
    def dealCard(individual):
        card = random.choice(deck)
        individual.append(card)

    #adding the card's value
    def total(individual):
        total = 0
        face = ["J", "Q", "K"]
        for card in individual:
            if card in range(1,11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total
    #Showing the dealer's hand depending on how many cards he has. 
    #If dealer has 2 cards, only show 1 card. If dealer has more than 2 cards, we could release all of his cards.
    def revealDealerHand():
        if len(dealerCards) == 2:
            return dealerCards[0]
        elif len(dealerCards) > 2:
            return dealerCards[0], dealerCards[1]

#Main Menu
    print("\n-------LET'S PLAY BLACKJACK!-------\n")
    while True:
        player_input = input("Press enter to play, or type in 'q' then enter to quit ")
        if player_input == "q":
            print("Goodbye!")
            quit()
        elif player_input == "":
            print("\nLet's begin...\n")
            time.sleep(2)
            break
        else:
            print("Invalid entry. Try again...")

    print("Dealer is passing out the cards...\n")
    time.sleep(2)

#Give the player and dealer 2 cards. Hide one of the dealer's card while showing both of the player's card
    for _ in range(2):
        dealCard(dealerCards)
        dealCard(playerCard)

    print(f"The dealer has [{revealDealerHand()}, Unknown card]\nValue: ?\n")
    time.sleep(2)

    print(f"You received {playerCard}\nValue: {total(playerCard)}\n")
    time.sleep(2)


#Player and dealer actions
    while player or dealer:
        if player:
            playerChoice = input("1: Stay\n2: Hit\n")
            if playerChoice == "1":
                player = False            
            
            else:
                time.sleep(2)
                dealCard(playerCard)
                print("\nThe dealer passes you another card...\n")
                time.sleep(2)
                print(f"Your hand:{playerCard}\nValue: {total(playerCard)}\n")
                time.sleep(2)
                if total(playerCard) > 21:
                    print("BUST!")
                    break
                elif total(playerCard) < 21:
                    continue

#Dealer will stop drawing if his value is higher than 16
        if total(dealerCards) > 16:
            dealer = False
        else:
            dealCard(dealerCards)
            time.sleep(2)
            print(f"\nDealer deals himself another card...\n")
            time.sleep(2)
            print(f"Dealer's hand: {dealerCards}\nValue: {total(dealerCards)}\n")
        
#If anyone gets the value of 21 or higher, break to Winning/Losing Determination Message 
# depending is it's a "bust" or "Blackjack/21"
        if total(playerCard) >= 21:
            break
        elif total(dealerCards) >= 21:
            break

#Winning/Losing Determination Message
    if total(playerCard) == 21:
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nBlackjack! You Win!")
    elif total(dealerCards) == 21:
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nBlackjack! Dealer Wins!")
    elif total(playerCard) > 21:
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nYou bust! Dealer Wins!")
    elif total(dealerCards) > 21:
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nDealer bust! You Win!")
    elif 21 - total(dealerCards) < 21 - total(playerCard):
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nDealer wins!")
    elif 21 - total(dealerCards) > 21 - total(playerCard):
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nYou win!")
    elif 21 - total(dealerCards) == 21 - total(playerCard):
        print(f"\nYou have {playerCard} with a total of {total(playerCard)}...")
        time.sleep(2)
        print(f"The dealer has {dealerCards} for a total of {total(dealerCards)}...")
        time.sleep(2)
        print(f"\nDraw!")

#Play again?
    playAgain = input("\n------------Play again?------------\nPress enter to go back to the main menu, or type 'q' then enter to quit ")
    if playAgain == "":
        continue
    elif playAgain == "q":
        quit()
    else:
        print("Invalid selection, try again.")