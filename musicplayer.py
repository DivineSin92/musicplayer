from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('MP3 Player')
root.iconbitmap('images/icon.ico')
root.geometry('450x300')

pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title = 'Choose a song', filetypes = (('mp3 Files', '*.mp3'), ))
    song = song.replace('F:/Programowanie/python/musicplayer/audio/', '')
    song = song.replace('.mp3', '')
    song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    song = f'F:/Programowanie/python/musicplayer/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

song_box = Listbox(root, bg = 'black', fg = 'green', width = 60, selectbackground = 'gray', selectforeground = 'black')
song_box.pack(pady = 20)

back_button_img = PhotoImage(file = 'images/Back.png')
stop_button_img = PhotoImage(file = 'images/Stop.png')
play_button_img = PhotoImage(file = 'images/Play.png')
pause_button_img = PhotoImage(file = 'images/Pause.png')
forward_button_img = PhotoImage(file = 'images/Forward.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image = back_button_img, borderwidth = 0)
stop_button = Button(controls_frame, image = stop_button_img, borderwidth = 0, command = stop)
play_button = Button(controls_frame, image = play_button_img, borderwidth = 0, command = play)
pause_button = Button(controls_frame, image = pause_button_img, borderwidth = 0)
forward_button = Button(controls_frame, image = forward_button_img, borderwidth = 0)

back_button.grid(row = 0, column = 0, padx = 10)
stop_button.grid(row = 0, column = 1, padx = 10)
play_button.grid(row = 0, column = 2, padx = 10)
pause_button.grid(row = 0, column = 3, padx = 10)
forward_button.grid(row = 0, column = 4, padx = 10)

my_menu = Menu(root)
root.config(menu = my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Add songs', menu = add_song_menu)
add_song_menu.add_command(label = 'Add Song', command = add_song)


root.mainloop()
