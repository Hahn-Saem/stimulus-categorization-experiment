import random
import datetime
import csv
import os
from config.config import Config

class Exp:
    def __init__(self, the_gui):
        self.the_gui = the_gui

        self.experiment_start_time = datetime.datetime.now()

        self.random_seed = None
        self.rng = random.Random()

        self.participant_id = None

        self.instruction_list = []

        self.full_stimulus_list = []

        self.data_list = []

        self.create_random_seed()
        self.create_participant_id()
        self.create_instruction_list()
        self.create_stimuli_list()
        self.the_gui.preload_images(self.full_stimulus_list)
        self.run_experiment()

    def create_random_seed(self):
        self.rng = random.Random(self.random_seed)
    
    def create_participant_id(self):
        formatted_datetime = self.experiment_start_time.strftime("%Y%m%d%H%M%S%f")
        random_number = self.rng.randint(100000, 999999)
        self.participant_id = f"{formatted_datetime}_{random_number}"

    def create_instruction_list(self):
        self.instruction_list = []

        with open("stimuli/instructions.txt", "r") as file:
            for line in file:
                line = line.strip("\n")

                line = line.replace(".", ".\n")

                self.instruction_list.append(line)

    def create_stimuli_list(self):
        directory_list = os.listdir("stimuli/images/")
        self.full_stimulus_list = []

        for thing in directory_list:
            if not thing.startswith("."):
                self.full_stimulus_list.append(thing[:-4])

    def run_experiment(self):
        self.the_gui.show_instructions(self.instruction_list[0], True)
        self.present_stimulus_list(self.full_stimulus_list, Config.test_key_list, True)
        self.the_gui.show_instructions(self.instruction_list[1], True)
        self.save_data()
        self.the_gui.root.destroy()

    def present_stimulus_list(self, stimulus_list, key_list, record_data):
        for stimulus_name in stimulus_list:
            key_pressed, rt = self.the_gui.show_stimulus(stimulus_name, key_list)
            if record_data:
                trial_data = [stimulus_name, key_pressed, rt]
                self.data_list.append(trial_data)
