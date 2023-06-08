from utils import *
from to_do_list_win import *
from to_do_list_mac import *

def main():
    cyan = "\033[1;36m"
    reset = "\033[0;0m"
    print(cyan + " _______      _____          _      _     _   ")
    print("|__   __|    |  __ \        | |    (_)   | |  ")
    print("   | | ___   | |  | | ___   | |     _ ___| |_ ")
    print("   | |/ _ \  | |  | |/ _ \  | |    | / __| __|")
    print("   | | (_) | | |__| | (_) | | |____| \__ \ |_ ")
    print("   |_|\___/  |_____/ \___/  |______|_|___/\__|")
    print(reset)    
    print('\n')
    print("Sur quel systeme d'exploitation êtes-vous ?")
    print("1. Windows")
    print("2. MacOS")
    print("3. Quitter")
    x = user_input()
    if x == "1":
        tdl_win()
    elif x == "2":
        tdl_mac()
    elif x == "3":
        print("Au revoir !")
        exit()

if __name__ == "__main__":
    main()