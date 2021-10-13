import random
import sys
import os

piles = []


def main():
    print("""
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
|W|I|S|H| |S|O|L|I|T|A|I|R|E|
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
1. Play wish solitaire
2. Load game
3. Quit""")

    choice = input(">")
    if choice not in ["1", "2", "3"]:
        print("Invalid input")
        main()
        return
    elif choice == "1":
        generateDeck()
        play()
        return
    elif choice == "2":
        loadGame()
    elif choice == "3":
        sys.exit(0)

def generateDeck():
    deck = []

    for i in ["\u2666", "\u2663", "\u2660", "\u2665"]:
        for j in ["7", "8", "9", "10", "J", "Q", "K", "A"]:
            deck.append([j] + [i])
    random.shuffle(deck)

    pile = []
    i = 0
    while i <= len(deck):
        if i in [4, 8, 12, 16, 20, 24, 28, 32]:
            piles.append(pile)
            pile = []

        if i == 32:
            break

        pile.append(deck[i])
        i += 1

    del deck


def displayInterface():
    print("\nA", "B", "C", "D", "E", "F", "G", "H", sep=(" "*5))
    for i in range(8):
        if not piles[i]:
            x = "X"
            print(f"{x:6}", end="")
        else:
            print(
                f"{piles[i][0][0]:2}{piles[i][0][1]:4}", end="")
    print()
    print(len(piles[0]), len(piles[1]), len(piles[2]),
          len(piles[3]), len(piles[4]), len(piles[5]),
          len(piles[6]), len(piles[7]), sep=(" "*5))
    print()


def evaluation():
    empty = True

    for i in piles:
        if i:
            empty = False
            break

    if empty:
        print()
        stopGame()
        print("---------------------------------------------")
        print("|  You won!                                 |")
        print("|  Press ENTER to go back to the main menu  |")
        print("---------------------------------------------")
        input()
        main()
        return

    lost = True
    for i in range(0, len(piles)):
        for j in range(1, len(piles)):
            try:
                if piles[i][0][0] == piles[j][0][0] and piles[i][0][1] == piles[j][0][1]:
                    pass
                elif piles[i][0][0] == piles[j][0][0]:
                    lost = False
                    break
            except:
                continue
        if not lost:
            break

    if lost:
        print()
        stopGame()
        print("---------------------------------------------")
        print("|  You lost!                                |")
        print("|  Press ENTER to go back to the main menu  |")
        print("---------------------------------------------")
        input()
        main()
        return


def play():
    evaluation()
    displayInterface()
    print("Press X to go back to the main menu")
    card1 = input("Choose the first card: ").upper()
    if card1 == "X":
        print()
        print("--------------------------------------")
        print("|  Do you want to save the game? Y/N |")
        print("--------------------------------------")
        print()
        save = input().upper()

        if save == "Y":
            saveGame()

        stopGame()
        main()
        return

    if card1 not in "ABCDEFGH" or len(card1) != 1:
        print("Invalid input")
        play()
        return

    card2 = input("Choose the second card: ").upper()

    if card2 == "X":
        print()
        print("---------------------------------------")
        print("|  Do you want to save the game? Y/N  |")
        print("---------------------------------------")
        print()
        save = input().upper()

        if save == "Y":
            saveGame()

        stopGame()
        main()
        return

    if (card2 not in "ABCDEFGH") or (len(card2) != 1) or (card1 == card2):
        print("Invalid input")
        play()
        return

    input2index = {"A": 0, "B": 1, "C": 2,
                   "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    card1, card2 = input2index[card1], input2index[card2]

    if not piles[card1] or not piles[card2]:
        print("The cards don't match")
        play()
        return
    else:
        if piles[card1][0][0] != piles[card2][0][0]:
            print("The cards don't match")
            play()
            return
        else:
            piles[card1].pop(0)
            piles[card2].pop(0)
            play()
            return()


def stopGame():
    global piles
    piles = []


def saveGame():
    print()
    with open("data.txt", "w", encoding="UTF-8") as f:
        for i in piles:
            output = ""
            for j in range(0, len(i)):
                output += str(i[j][0] + "-" + i[j][1]) + " "
            f.write(str(output) + "\n")
    print("-"*54)
    print("  Created savegame in", os.getcwd())
    print("-"*54)
    print()


def loadGame():
    if not os.path.isfile("data.txt"):
        print("-"*54)
        print("  Can't find data.txt in", os.getcwd())
        print("  Press ENTER to go back to the main menu")
        print("-"*54)
        input()
        main()
        return
    else:
        global piles
        with open("data.txt", "r", encoding="UTF-8") as f:
            stokknr = 0
            piles = [[], [], [], [], [], [], [], []]
            for line in f:
                if stokknr == 8:
                    break
                else:
                    for j in line.split():
                        kort = j.split("-")
                        kort = [kort[0], kort[1]]
                        piles[stokknr].append(kort)
                    stokknr += 1
        print("-"*60)
        print(f"  Loading savegame from {os.getcwd()}\\data.txt")
        print("-"*60)
        play()
        return


main()
