from functions import *

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
    elif choice == "1":
        newGame()
    elif choice == "2":
        loadGame()
    elif choice == "3":
        # Terminating the program
        sys.exit(0)
    
    main()

if __name__ == "__main__":
    main()