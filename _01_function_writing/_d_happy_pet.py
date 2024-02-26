"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    pet = simpledialog.askstring(title= 'free robux', prompt= ' What pet do u want?????? (choose from a dog, cat, fish, a snake, a turtle, a rabbit, or a Kanye')
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with

    #      their pet until the desired pet happiness level has been reached.

    happiness = 0
    while happiness < 10:
        action = simpledialog.askstring(title= 'wsg', prompt= 'Do you want to play, swim,or be a good person')
        if action == 'play':
            happiness += 5
            messagebox.showinfo(title='Wsg bruv', prompt = 'your pets happiness increased  by 5, u need 5 more points to win the game!')
        elif action == 'swim':
            happiness += 4
            messagebox.showinfo(title= ' AYO', prompt = 'your pets happiness increased by 4, u need 6 more points to beat the game! ')
        elif action == 'be a good person' and pet == 'Kanye':
            messagebox.showinfo(title = 'wsg good, dont be grant', prompt = ' Kanye is mad at u for being a good person, and attacks. U lost all points')
            happiness -= 0
        elif action == 'be a good person' and pet == 'dog' and pet == 'cat' and pet == 'turtle' and pet == 'snake' and pet == 'rabbit' and pet == 'fish':
            happiness += 10
            messagebox.showinfo(title= ' free robux', prompt = 'You got 10 happiness points, AKA the goal for this game')






    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
