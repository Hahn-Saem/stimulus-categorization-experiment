import tkinter as tk
from config.config import Config
import time
from PIL import Image, ImageTk
import os

class Gui:
    def __init__(self) -> None:
        """
        Initializes the GUI variables and calls the methods needed to set up the GUI.

        Args:
            None
        
        Returns:
            None
        """
        self.root = None
        self.stimulus_frame = None
        self.stimulus_label1 = None
        self.stimulus_label2 = None
        self.target_word_label = None
        self.instructions__text_label = None
        self.key_pressed = None
        self.image_dict = None

        self.create_window()
        self.create_labels()

    def create_window(self) -> None:
        """
        Create the window for the experiment.

        Args:
            None

        Returns:
            None
        """
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(Config.window_width, Config.window_height))  
        self.root.title("Stimulus Categorization Experiment")
        self.root.configure(bg="white")
        self.root.resizable(False, False) 

    def create_labels(self) -> None:
        """
        Create the instructions label, stimulus frame, stimulus labels, and target word label.

        Args:
            None

        Returns:
            None
        """
        self.instructions_text_label = tk.Label(
            self.root,
            height=Config.window_height,
            width=Config.window_width,
            bg=Config.instructions_bg_color,
            fg=Config.instructions_font_color,
            font="{} {}".format(Config.instructions_font, Config.instructions_font_size)
        )

        self.stimulus_frame = tk.Label(
            self.root,
            bg = Config.stimulus_bg_color
        )

        self.stimulus_label1 = tk.Label(
            self.stimulus_frame,
            bg=Config.stimulus_bg_color,
            fg=Config.stimulus_font_color,
            font="{} {}".format(Config.stimulus_font, Config.stimulus_font_size)
        )

        self.stimulus_label2 = tk.Label(
            self.stimulus_frame,
            bg=Config.stimulus_bg_color,
            fg=Config.stimulus_font_color,
            font="{} {}".format(Config.stimulus_font, Config.stimulus_font_size)
        )

        self.target_word_label = tk.Label(
            self.root, 
            anchor='center',
            bg=Config.target_word_bg_color,
            fg=Config.target_word_font_color,
            font="{} {}".format(Config.target_word_font, Config.target_word_font_size)
        )

    def preload_images(self, image_name_list: list[list[str]]) -> None:
        """
        Preload and configure all the images into a dictionary.

        Args:
            image_name_list (list[list[str]]): a list of lists, where each inner list contains the names of all
            the images in a stimulus set.

        Returns:
            None
        """
        self.image_dict = {}

        directory_list = os.listdir("stimuli/images/")

        for file, set in zip(directory_list, image_name_list):
            current_file = "stimuli/images/" + file + "/"
            for img in set:
                image = Image.open(current_file + img + ".png")

                image = image.resize(
                    (Config.image_stimulus_width, Config.image_stimulus_height)
                )
                photo_image = ImageTk.PhotoImage(image)
                self.image_dict[img] = photo_image
    
    def show_instructions(self, instructions: str, end_on_key_press: bool, extra_delay: int = None) -> None:
        """
        Display instructions to the participant.

        Args:
            instructions (str): the instruction(s) to display.
            end_on_key_press (bool): whether to wait for a key press to end the instruction display.
            extra_delay (int, optional): an additional delay before ending the instruction display.

        Returns:
            None
        """
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

    def check_for_valid_key_press(self, event: tk.Event, valid_keys: list[str]) -> None:
        """
        Check whether the key pressed by the participant is a valid key to end the instruction display.

        Args:
            event (tk.Event): the key press event.
            valid_keys (list[str]): a list of valid key(s) that can end the instruction display.

        Returns:
            None
        """
        if event.keysym in valid_keys:
            self.root.unbind('<Key>')

            self.root.focus_set()

            self.key_pressed = event.keysym  
    
    def show_target_word(self, target_word: str) -> None:
        """
        Display the target word for a set amount of time.

        Args:
            target_word (str): the target word to display.
        
        Returns:
            None
        """
        self.target_word_label.configure(text=target_word) 
        self.target_word_label.pack(expand=True)
        self.target_word_label.pack_propagate(False)

        self.root.update()
        
        self.root.after(Config.target_word_delay)

        self.target_word_label.pack_forget() 

    def show_stimulus(self, left_stimuli: str, right_stimuli: str, key_list: list[str]) -> tuple[str, float]:
        """
        Display the stimuli the proper side of the screen.

        Args:
            left_stimuli (str): the name of the stimulus to display on the left-hand side of the screen.
            right_stimuli (str): the name of the stimulus to display on the right-hand side of the screen.
            key_list (list[str]): a list of strings, where each string represents a key that can be pressed.

        Returns:
            tuple[str, float]: a tuple containing the key pressed and the reaction time.
        """
        self.stimulus_label1.configure(image=self.image_dict[left_stimuli])
        self.stimulus_label2.configure(image=self.image_dict[right_stimuli])

        self.stimulus_label1.pack(side="left")
        self.stimulus_label2.pack(side="right")

        self.stimulus_frame.pack(expand=True, fill="both")
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

        self.stimulus_frame.pack_forget()
        self.root.update()

        return self.key_pressed, rt