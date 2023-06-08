from utils_fr import *
from utils_eng import *
from to_do_list_win_fr import *
from to_do_list_mac_fr import *
from to_do_list_win_eng import *
from to_do_list_mac_eng import *
from language import *
from os import name as os_name

def main():
    a = language()
    if a == "1":
        if os_name == "nt":
            tdl_win_fr()
        else:
            tdl_mac_fr()
    elif a == "2":
        if os_name == "nt":
            tdl_win_eng()
        else:
            tdl_mac_eng()

if __name__ == "__main__":
    main()