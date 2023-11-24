import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Load custom button images
        play_button_image = Image.open("play_button.png")
        play_button_photo = ImageTk.PhotoImage(play_button_image)

        pause_button_image = Image.open("pause_button.png")
        pause_button_photo = ImageTk.PhotoImage(pause_button_image)

        browse_button_image = Image.open("browse_button.png")
        browse_button_photo = ImageTk.PhotoImage(browse_button_image)

        # Create round and transparent buttons
        self.play_button = tk.Button(root, image=play_button_photo, command=self.toggle_play_pause, bd=0, relief="flat", bg="#ff7556" , highlightthickness=0)
        self.play_button.photo = play_button_photo
        self.play_button.place(relx=0.45, rely=0.5)

        self.browse_button = tk.Button(root, image=browse_button_photo, command=self.browse_audio, bd=0, relief="flat", bg="#ff7556", highlightthickness=0)
        self.browse_button.photo = browse_button_photo
        self.browse_button.place(relx=0.45, rely=0.9)

        self.audio_file = None
        self.playing = False

    def browse_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")])
        if file_path:
            self.audio_file = file_path

    def toggle_play_pause(self):
        if self.audio_file:
            if not self.playing:
                pygame.mixer.init()
                pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
                self.playing = True
                self.play_button.config(image=self.play_button.photo)  # Set the "Pause" image
            else:
                pygame.mixer.music.pause()
                self.playing = False
                self.play_button.config(image=self.play_button.photo)  # Set the "Play" image
        else:
            messagebox.showerror("Error", "Please select an audio file first")

if __name__ == "__main__":
    root = tk.Tk()
    background_image = ImageTk.PhotoImage(Image.open("background.png"))
    tk.Label(root, image=background_image).pack()
    player = AudioPlayer(root)
    root.mainloop()
