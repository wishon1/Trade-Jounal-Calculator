#!/usr/bin/env python3
import sys
import cmd
# from Base_mode.Base_clase import BaseClass


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
        1: 'Cryptocurrency', 2: 'Indices',
        3: 'Commodities', 4: 'Stock Index', 5: 'Forex', 6: 'Trade statistics'
    }

    def default(self, line):
        """print, if it's in the interactive mode"""
        if sys.stdin.isatty():
            print("\t\t--------------Trade Jounal version 1.0 ------------")
            for key, value in self.class_option.items():
                print("{}: {}".format(key, value))
            option = input("Enter a number to select: ")
            
            # check if the lenth of the input is more that 2
            if len(option) == 0 or len(option) > 1:
                print("Invalid input")
            else:
                option = int(option)

            # check if the option is in the dict()
            if option in TradeJournal.class_option.key():
                if option == 1:
                    new_instance = Crytocurrency()
                elif option == 2:
                    new_instance = Indices()
                elif option == 3:
                    new_instance = Commodities()
                elif option == 4:
                    new_instance = StockIndex()
                elif option == 5:
                    new_instance = Forex()
                elif option == 6:
                    new_instance = TradeStatistics()

                else:
                    print("<<< {} is invalid, please select between 1 - 6 >>>"
                         .format(option))
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
