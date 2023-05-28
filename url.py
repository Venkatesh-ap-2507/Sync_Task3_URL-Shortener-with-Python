import pyshorteners
import tkinter as tk
import pyperclip

def shorten_url():
   
    long_url = input_field.get()

    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    pyperclip.copy(short_url)

    output_field.delete(0, tk.END)
    output_field.insert(0, short_url)


root = tk.Tk()
root.title("URL Shortener")

title_label = tk.Label(root, text="Enter Your URL")
title_label.pack()


input_field = tk.Entry(root, width=50)
input_field.pack()


shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack()

output_field = tk.Entry(root, width=50)
output_field.pack()

copyButton = tk.Button(root,text='Copy')
copyButton.pack(pady=5)


root.mainloop()
