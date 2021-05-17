import random

completeDeck = [11, 11, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2] # All of the values in the deck, aces are stored as 11 and get changed to 1 in hand when the player would bust
options = ['H', 'S'] # H = Hit, S = Stand

# key = dealer's card, value = dictionary of player hand total keys and option values
hardHands = {
    2: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'S', 14:'S', 15:'S', 16:'S', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    3: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'S', 14:'S', 15:'S', 16:'S', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    4: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'S', 13:'S', 14:'S', 15:'S', 16:'S', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    5: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'S', 13:'S', 14:'S', 15:'S', 16:'S', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    6: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'S', 13:'S', 14:'S', 15:'S', 16:'S', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    7: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    8: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    9: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    10: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'},
    11: {4:'H', 5:'H', 6:'H', 7:'H', 8:'H', 9:'H', 10:'H', 11:'H', 12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'S', 18:'S', 19:'S', 20:'S', 21:'S'}
}

# key = dealer's card, value = dictionary of player hand high total and option values
softHands = {
    2: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    3: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    4: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    5: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    6: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'H', 20:'S', 21:'S'},
    7: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'S', 19:'S', 20:'S', 21:'S'},
    8: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'S', 19:'S', 20:'S', 21:'S'},
    9: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    10: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'},
    11: {12:'H', 13:'H', 14:'H', 15:'H', 16:'H', 17:'H', 18:'H', 19:'S', 20:'S', 21:'S'}
}

# Gets the total value of a list of integers (i.e. a blackjack hand)
def total(list):

    total = 0
    for i in list:
        total += i

    return total

# This method is a work in progress
def playBasic(hands):

    # Net number of hands won or lost
    results = 0

    for i in range(hands):

        playerHand = [] # The hand of the player
        dealerHand = [] # The hand of the dealer

        deck = completeDeck.copy() # Copy the deck
        random.shuffle(deck) # Shuffle the copy of the deck

        playerHand.append(deck.pop(0))
        dealerHand.append(deck.pop(0))
        playerHand.append(deck.pop(0))
        dealerHand.append(deck.pop(0))

        softHand = False
        if(11 in playerHand):
            softHand = True
            if(total(playerHand) == 22):
                playerHand[0] = 1
        end = False
        while(not end):
            if(softHand): # Uses soft hand lookup table if soft hand
                if(softHands[dealerHand[0]][total(playerHand)] == 'H'): # Executes if the lookup table says to Hit
                    playerHand.append(deck.pop(0))
                    if(total(playerHand)>21):
                        for i in range(len(playerHand)):
                            if(playerHand[i] == 11):
                                playerHand[i] = 1
                                break                        
                    if(not 11 in playerHand):
                        softHand = False
                else:
                    end = True # Ends player loop because player Stands
            else: # Uses hard hand lookup table
                if(hardHands[dealerHand[0]][total(playerHand)] == 'H'): # Executes if the lookup table says to Hit
                    playerHand.append(deck.pop(0))
                    if(total(playerHand)>21):
                        if(playerHand[len(playerHand)-1] == 11): # If the Hit is an Ace and 11 would make the player bust
                            playerHand[len(playerHand)-1] = 1 # Set the Ace to 1
                        else:
                            end = True # Player busts
                    if(11 in playerHand):
                        softHand = True # Player has an unmodified Ace, so now the hand is a soft hand
                else:
                    end = True # Ends player loop because player Stands
        
        if(total(playerHand) > 21):
            results -= 1 # Player loses if they bust
        elif(total(dealerHand) >= 17 and total(dealerHand) <= 21): # The dealer stands on 17 or higher, and then the player and dealer compare hands
            if(total(playerHand) > total(dealerHand)):
                results += 1
            elif(total(playerHand) == total(dealerHand)):
                results += 0
            else:
                results -= 1
        else:
            if(total(dealerHand) == 22):
                dealerHand[1] = 1 # Dealer has 2 Aces, set second Ace value to 1
            while(total(dealerHand) < 17): # The dealer hits until they reach 17 or higher
                dealerHand.append(deck.pop(0))
                if(total(dealerHand) > 21):
                    dealerHand.sort()
                    if(dealerHand[len(dealerHand)-1] == 11):
                        dealerHand[len(dealerHand)-1] = 1
            if(total(dealerHand) > 21): # If dealer busts, the player wins
                results += 1
            elif(total(playerHand) > total(dealerHand)): # If the player hand is worth more than the dealer hand, the player wins
                results += 1
            elif(total(playerHand) == total(dealerHand)): # If both hands are equal, the player and the dealer draw/push
                results += 0
            else:
                results -= 1 # Otherwise, the player loses
    
    return results


# This is a baseline strategy for a player that always stands on their 2 cards no matter what
def playAlwaysStand(hands):

    results = 0

    for i in range(hands):

        playerHand = [] # The hand of the player
        dealerHand = [] # The hand of the dealer

        deck = completeDeck.copy() # Copy the deck
        random.shuffle(deck) # Shuffle the copy of the deck

        playerHand.append(deck.pop(0)) # Deal player first card
        dealerHand.append(deck.pop(0)) # Deal dealer first card
        playerHand.append(deck.pop(0)) # Deal player second card
        dealerHand.append(deck.pop(0)) # Deal dealer second card

        if(total(playerHand) == 22):
            playerHand[0] = 1
        elif(total(dealerHand) >= 17 and total(dealerHand) <= 21): # The dealer stands on 17 or higher, and then the player and dealer compare hands
            if(total(playerHand) > total(dealerHand)):
                results += 1
            elif(total(playerHand) == total(dealerHand)):
                results += 0
            else:
                results -= 1
        else:
            if(total(dealerHand) == 22):
                dealerHand[1] = 1 # Dealer has 2 Aces, set second Ace value to 1
            while(total(dealerHand) < 17): # The dealer hits until they reach 17 or higher
                dealerHand.append(deck.pop(0))
                if(total(dealerHand) > 21):
                    dealerHand.sort()
                    if(dealerHand[len(dealerHand)-1] == 11):
                        dealerHand[len(dealerHand)-1] = 1
            if(total(dealerHand) > 21): # If dealer busts, the player wins
                results += 1
            elif(total(playerHand) > total(dealerHand)): # If the player hand is worth more than the dealer hand, the player wins
                results += 1
            elif(total(playerHand) == total(dealerHand)): # If both hands are equal, the player and the dealer draw
                results += 0
            else:
                results -= 1 # Otherwise, the player loses
    
    return results


print("Basic Strategy Lookup Player Edge:")
print("----------------------------------------------------------")
print(str((playBasic(50000) + playBasic(50000) + playBasic(50000) + playBasic(50000) + playBasic(50000)) / 5.0 / 50000 * 100) + "%")
print()
print("Always Stand Player Edge:")
print("----------------------------------------------------------")
print(str((playAlwaysStand(50000) + playAlwaysStand(50000) + playAlwaysStand(50000) + playAlwaysStand(50000) + playAlwaysStand(50000)) / 5.0 / 50000 * 100) + "%")