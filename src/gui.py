import tkinter as tk
from config.config import Config
import time
from PIL import Image, ImageTk
import os

class Gui:
    def __init__(self):
        self.root = None
        self.stimulus_label = None
        self.instructions_label = None
        self.key_pressed = None
        self.image_dict = None

        self.create_window()
        self.create_labels()

    def create_window(self):
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(Config.window_width, Config.window_height))  
        self.root.title("Stimulus Categorization Experiment")
        self.root.configure(bg="white")
        self.root.resizable(False, False) 

    def create_labels(self):
        self.instructions_text_label = tk.Label(
            self.root, anchor='center',
            height=Config.window_height,
            width=Config.window_width,
            bg=Config.instructions_bg_color,
            fg=Config.instructions_font_color,
            font="{} {}".format(Config.instructions_font, Config.instructions_font_size)
        )

        # change this so that label only takes up half of the screen
        self.stimulus_label = tk.Label(
            self.root, anchor='center',
            height=Config.window_height,
            width=Config.window_width,
            bg=Config.stimulus_bg_color,
            fg=Config.stimulus_font_color,
            font="{} {}".format(Config.stimulus_font, Config.stimulus_font_size)
        )
    def preload_images(self, image_name_list):
        self.image_dict = {}
        directory_list = os.listdir("stimuli/images/")
        for file, set in zip(directory_list, image_name_list):
            current_file = "stimuli/images/" + file + "/"
            for img in set:
                image = Image.open(current_file + img + ".png")
                photo_image = ImageTk.PhotoImage(image)
                self.image_dict[img] = photo_image
    
    def show_instructions(self, instructions, end_on_key_press, extra_delay=None):
        self.instructions_text_label.configure(text=instructions) 
        self.instructions_text_label.pack()
        self.instructions_text_label.pack_propagate(False)
        self.root.update()  

        if end_on_key_press:  
            self.key_pressed = None  

            self.root.bind('<Key>', lambda event: self.check_for_valid_key_press(event, ["space"]))

            while not self.key_pressed:
                self.root.update()
        else: 
            self.root.after(Config.instruction_delay)

        if extra_delay is not None:
            self.root.after(extra_delay)

        self.instructions_text_label.pack_forget() 
        self.root.update()

    def check_for_valid_key_press(self, event, valid_keys):
        if event.keysym in valid_keys:

            self.root.unbind('<Key>')

            self.root.focus_set()

            self.key_pressed = event.keysym  
        
    def show_stimulus(self, stimulus1, stimulus2, key_list):
        self.stimulus_label.configure(image=self.image_dict[stimulus1])
        self.stimulus_label.pack(side=tk.LEFT)
        self.stimulus_label.pack_propagate(False)
        self.root.update()

        time1 = time.time()

        self.key_pressed = None
        self.root.bind(
            '<Key>',
            lambda event: self.check_for_valid_key_press(event, key_list)
        )

        while not self.key_pressed:
            self.root.update()

        time2 = time.time()
        rt = time2 - time1

        self.stimulus_label.pack_forget()
        self.root.update()

        return self.key_pressed, rt