# Importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

# Creating the root window
root = Tk()
root.title('DataFlair Python MP3 Music Player App')

# Initialize mixer
mixer.init()

# Function definitions
def Play():
    # Function to play the selected song
    pass

def Pause():
    # Function to pause the currently playing song
    pass

# Create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Font is defined which is to be used for the button font
defined_font = font.Font(family='Helvetica')

# Play button
play_button = Button(root, text="Play", width=7, command=Play)
play_button['font'] = defined_font
play_button.grid(row=1, column=0)

# Pause button
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1)

# Run the main loop
root.mainloop()
