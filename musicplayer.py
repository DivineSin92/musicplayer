from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3

root = Tk()
root.title('MP3 Player')
root.iconbitmap('images/icon.ico')
root.geometry('300x450')

pygame.mixer.init()

def timer():
    times = pygame.mixer.music.get_pos() / 1000
    converted_time = time.strftime('%M:%S', time.gmtime(times))
    song = song_box.get(ACTIVE)
    song = f'F:/Programowanie/python/musicplayer/audio/{song}.mp3'
    song_mut = MP3(song)
    song_leng = song_mut.info.length
    leng_time = time.strftime('%M:%S', time.gmtime(song_leng))
    status_bar.config(text = f'{converted_time}/{leng_time}')
    status_bar.after(1000, timer)

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title = 'Choose a song', filetypes = (('mp3 Files', '*.mp3'), ))
    song = song.replace('F:/Programowanie/python/musicplayer/audio/', '')
    song = song.replace('.mp3', '')
    song_box.insert(END, song)

def add_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title = 'Choose a song', filetypes = (('mp3 Files', '*.mp3'), ))
    for song in songs:
        song = song.replace('F:/Programowanie/python/musicplayer/audio/', '')
        song = song.replace('.mp3', '')
        song_box.insert(END, song)

def del_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def del_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

global paused
paused = False

def play():
    global paused

    song = song_box.get(ACTIVE)
    song = f'F:/Programowanie/python/musicplayer/audio/{song}.mp3'

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops = 0)

    timer()

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.config(text = '')

def pause(is_paused):
    global paused
    paused = is_paused
    
    pygame.mixer.music.pause()
    paused = True

def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    song = f'F:/Programowanie/python/musicplayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last = None)

def prev_song():
    next_one = song_box.curselection()
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    song = f'F:/Programowanie/python/musicplayer/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last = None)

song_box = Listbox(root, bg = 'black', fg = 'white', width = 47, height = 20, selectbackground = 'gray', selectforeground = 'black')
song_box.pack(pady = 10)

back_button_img = PhotoImage(file = 'images/Back.png')
stop_button_img = PhotoImage(file = 'images/Stop.png')
play_button_img = PhotoImage(file = 'images/Play.png')
pause_button_img = PhotoImage(file = 'images/Pause.png')
forward_button_img = PhotoImage(file = 'images/Forward.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image = back_button_img, borderwidth = 0, command = prev_song)
stop_button = Button(controls_frame, image = stop_button_img, borderwidth = 0, command = stop)
play_button = Button(controls_frame, image = play_button_img, borderwidth = 0, command = play)
pause_button = Button(controls_frame, image = pause_button_img, borderwidth = 0, command = lambda: pause(paused))
forward_button = Button(controls_frame, image = forward_button_img, borderwidth = 0, command = next_song)

back_button.grid(row = 0, column = 0, padx = 2)
stop_button.grid(row = 0, column = 1, padx = 2)
play_button.grid(row = 0, column = 2, padx = 2)
pause_button.grid(row = 0, column = 3, padx = 2)
forward_button.grid(row = 0, column = 4, padx = 2)

my_menu = Menu(root)
root.config(menu = my_menu)

music_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = 'Menu', menu = music_menu)
music_menu.add_command(label = 'Add Song', command = add_song)
music_menu.add_command(label = 'Add Songs', command = add_songs)
music_menu.add_separator()
music_menu.add_command(label = 'Del Selected Song', command = del_song)
music_menu.add_command(label = 'Del All Songs', command = del_all_songs)

status_bar = Label(root, text = '', bd = 1, relief = GROOVE, anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 2)


root.mainloop()
