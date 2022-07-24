from passwords import *

# class for using a cli-interface
class Interface():
    def __init__(self):
        self.string = str()
        print("\nHello, this is Gamayun!\
        \nI'm password manager.\
        \nType 'help' to see what I can\n")
        
        # Cycle for taking input from user
        while self.string != "exit":
            self.string = input("> ")
        
            if self.string == "help": # help tips
                print("\nThe options are:\
                \n\nhelp - to show this option\
                \nnew - to create new password\
                \nlist - to list all passwords\
                \nchange - to change password\
                \nremove - to delete password\n")

            # options choosing statement
            elif self.string == "new": # creates new password
                self._new()
            elif self.string == "list": # lists passwords
                self._list()
            elif self.string == "change": # changes password
                self._change()
            elif self.string == "remove": # remove password
                self._delete()
            else:
                pass
    
    # Creating new password
    def _new(self):
        print()
        name = input("\nEnter new password's name: ")
        size = int(input("Enter new password's length: "))
        style = input("Enter new password's style(mix, letters, numbers): ")
        print()

        # assignment of password
        Passwords._new(style, size, name)
         
    # List of all the passwords
    def _list(self):
        print()
        [print(key,':',value) for key, value in Passwords.passwords.items()]
        print()

    # Changing of password
    def _change(self):
        if Passwords.passwords: # handling passwords absence 
            self._list()
            name = input("Which one should be changed: ")

            while not (name in Passwords.passwords.keys()): # checking for presence
                name = input(f"There is no {name}. Enter again: ")
                
            # Loop for taking user options on creating new password
            while True:
                do = input("Do you want gamayun to generate new password?(Y/n): ")
                if do == "Y":
                    size = int(input("Enter new password's length: "))
                    style = input("Enter new password's style(mix, letters, numbers): ")
                    Passwords._change_auto(name, style, size)
                    break

                elif do == "n":
                    entered_password = input("Enter new password: ")
                    Passwords._change_manualy(name, entered_password) 
                    break
                
                else:
                    print("You have no such option")

        else: print("You have no passwords to change!")
        print()

    # Deletion of password
    def _delete(self):
        self._list()
        name = input("Enter which password to delete: ")
        Passwords._delete(name)

# Main part of program
defined = Interface()
