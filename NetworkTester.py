#!/usr/bin/python3

import tkinter as tk
from ping3 import ping, verbose_ping

def ping_test():
    try:
        result = ping("8.8.8.8")
        if result is not None:
            print(f"Ping Successfull: {result}")
        else:
            print(f"Ping has failed: {result}")
    except Exception as e:
        print(f"An unexpected error has occured: {str(e)}")


window = tk.Tk()
window.title("Network Tester")
window.geometry("400x400")

button = tk.Button(window, text="Ping", command=ping_test)
button.pack(side='top', anchor='nw', ipadx=40, padx=15, pady=10)

window.mainloop()
