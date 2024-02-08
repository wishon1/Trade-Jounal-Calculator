#!/usr/bin/env python3
import sys
import cmd

class TradeJournal(cmd.Cmd):
    """
    This class contains all the functionalities for the TradeJournal console
    """
    # The prompt for the interactive and non-interactive mode
    if sys.stdin.isatty():
        prompt = "\t\t--------------WELCOME TO ALGOMERIX TRADE JOURNAL---------"
    else:
        prompt = ''

    class_option = {
        1: 'Cryptocurrency', 2: 'Indice',
        3: 'Commodities', 4: 'Stock Index', 5: 'Forex', 6: 'Trade statistics'
    }

    def precmd(self, line):
        """print, if it's in the interactive mode"""
        if sys.stdin.isatty():
            print("\t\t--------------Please enter a number to select------------")
            option = []
            for key, value in self.class_option.items():
                print("{}: {}".format(key, value))
            option = int(input("Enter a number to select: "))

            if len(option) > or < 1:
                print("Invalid input")
            else:
                for key, value in self.class_option.items():
                    if option == key:
                    print("You just selected: {}".format(value)
                else:
                    print("invalid syntax")

        return line
 
    def do_quit(self, command):
        """the method to exit the isatty phase when exit is entered"""
        exit()
    
    def do_EOF(sef, arg):
        """ Handles EOF in order to exit the console"""
        print()
        exit()
    
    def help(self):
        """ The methods prints the help documentation for quit"""
        print("Exiting the program...\n")

if __name__ == "__main__":
    TradeJournal().cmdloop()
