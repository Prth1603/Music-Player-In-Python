#music player in python
from tkinter import *
import pygame
import time
from tkinter import filedialog
import random
import os
from tkinter import ttk
from mutagen.mp3 import MP3

root = TK()
root.title("Pheonixxx music")
root.geometry("700x300")

#initiate pygame mixer
pygame.mixer.init()

#song_length info
def play_time():
    if stopped:
        return
    curr_time = pygame.mixer.music.get_pos() // 1000
    song = song_box.get(ACTIVE)
    song = f'{head}/{song}.mp3'
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    if int(my_slider.get()) == int(song_length):
        song_no = song_box.curselection()[0] + 1
        if song_no == song_box.size():
            song_no = 0
          song = song_box.get(song_no)
        song = f'{head}/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        song_box.selection_clear(ACTIVE)
        song_box.selection_set(song_no)
        slide(0)

    elif paused:
        pass
    elif int(my_slider.get()) == curr_time:
        slider_pos = int(song_length)
        my_slider.config(to=slider_pos, value=curr_time)
    else:
        slider_pos = int(song_length)
        my_slider.config(to=slider_pos, value=int(mu_slider.get())

        new_time = int(my_slider.get()) + 1
        my_slider.config(value=new_time)

    s_len = time.strftime('%M:%S', time.gmtime(song_length))
    new_time = time.strftime('%M:%S', time.gmtime(my_slider.get())
    slider_label.config(text=f'{new_time} / {s_len}')

    status_bar.after(1000, play_time)

# add song func
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audios/', title="Choose...", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        global head
        global tail
        head, tail = os.path.split(song)
        song_box.insert(END, tail[:-4])


                                                      
                        
  
 
