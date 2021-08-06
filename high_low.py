
import random

scores = []

for t in range(1, 4):
    hearts = ["2 ♥︎", "3 ♥︎", "4 ♥︎", "5 ♥︎", "6 ♥︎", "7 ♥︎", "8 ♥︎", "9 ♥︎", "10 ♥︎", "Jack ♥︎", "Queen ♥︎", "King♥︎", "Ace ♥︎"]
    spades = ["2 ♠︎", "3 ♠︎", "4 ♠︎", "5 ♠︎", "6 ♠︎", "7 ♠︎", "8 ♠︎", "9 ♠︎", "10 ♠︎", "Jack ♠︎", "Queen ♠︎", "King ♠︎", "Ace ♠︎"]
    diamonds = ["2 ♦︎", "3 ♦︎", "4 ♦︎", "5 ♦︎", "6 ♦︎", "7 ♦︎", "8 ♦︎", "9 ♦︎", "10 ♦︎", "Jack ♦︎", "Queen ♦︎", "King ♦︎", "Ace ♦︎"]
    clubs = ["2 ♣︎", "3 ♣︎", "4 ♣︎", "5 ♣︎", "6 ♣︎", "7 ♣︎", "8 ♣︎", "9 ♣︎", "10 ♣︎", "Jack ♣︎", "Queen ♣︎", "King ♣︎", "Ace ♣︎"]

    allcards = [hearts, spades, diamonds, clubs]
    score = 0
    deck = random.choice(allcards)
    card1 = random.choice([x for x in deck if x != "nt"])
    print(card1)

    while True:
        pl_choice = input("High or Low? ").strip()

        num1 = deck.index(card1)
        deck[num1] = "nt"

        deck = random.choice(allcards)
        card2 = random.choice([x for x in deck if x != "nt"])
        num2 = deck.index(card2)
        print(card2)

        if pl_choice.lower() == "high" and num2 > num1:
            card1 = card2
            score += 1
            pass
        elif pl_choice.lower() == "low" and num2 < num1:
            card1 = card2
            score += 1        
            pass
        elif num1 == num2:
            card1 = card2
            score += 1

        else:
            print("This turn is over")
            print("Score: ", score)
            scores.append(score)
            print("let's play again")
            print("================")
            break

best_score = max(scores)
print("Your best score is: ", best_score)