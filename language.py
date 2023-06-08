from utils_fr import user_input

def language():
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
    print("1. Français")
    print("2. English")
    a = user_input()
    return a