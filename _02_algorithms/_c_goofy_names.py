"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    tenge  = simpledialog.askstring(title='wsg ', prompt='What be ur name, sonny boi????')
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of  name has been constructed.
    fh =''
    for i in range(len((tenge))):
        fh +=tenge[i].upper()

    print(fh)







    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    pass
