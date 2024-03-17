"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    num = simpledialog.askstring(title= 'wsg bruv', prompt= 'Enter a number pls')
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime
    num = int(num)
    max = (num//2)
    primes = []
    for x in range (2,max):
        if num %x == 0:
            messagebox.showinfo(title='hi', message= 'your num isnt prime ')
        else:
            primes.append(num)





    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass

