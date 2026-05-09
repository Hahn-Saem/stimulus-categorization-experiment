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

        self.full_stimuli_list = []

        self.data_list = []

        self.create_random_seed()
        self.create_participant_id()
        self.create_instruction_list()
        self.create_stimuli_list()
        self.the_gui.preload_images(self.full_stimuli_list)
        self.run_experiment()

    def create_random_seed(self):
        self.random_seed = int(self.experiment_start_time.strftime("%Y%m%d%H%M%S%f"))
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
        self.full_stimuli_list = []

        # Adds all the stimuli sets to self.full_stimuli_list. 
        # Note: this does NOT add all the images individually, but the folders containing the stimuli sets
        for file in directory_list:
            curr_dir = os.listdir("stimuli/images/" + file + "/")
            img_set = []
            for img in curr_dir:
                if not file.startswith("."):
                    img_set.append(img[:-4])
            self.full_stimuli_list.append(img_set)

    def run_experiment(self):
        self.the_gui.show_instructions(self.instruction_list[0], True)
        self.present_stimulus_list(self.full_stimuli_list, Config.test_key_list)
        self.the_gui.show_instructions(self.instruction_list[1], True)
        # self.save_data()
        self.the_gui.root.destroy()

    def present_stimulus_list(self, stimulus_list, key_list): 
        full_stimulus_pairings_list = []

        for target_word in Config.target_word_list:
            stimuli_set_list = []
            target_word = target_word.lower()

            # Find where the folder where the target stimulus is located
            for stimuli_set in stimulus_list:
                if target_word in stimuli_set:
                    stimuli_set_list = stimuli_set
                    stimuli_set_list.remove(target_word)
                    break

            for distractor_word in stimuli_set_list:
                full_stimulus_pairings_list.append({
                    "left": target_word,
                    "right": distractor_word
                })

                full_stimulus_pairings_list.append({
                    "left": distractor_word,
                    "right": target_word
                })
        
        random.shuffle(full_stimulus_pairings_list)

        for trial in full_stimulus_pairings_list:
            if trial["left"] in Config.target_word_list:
                target_word = trial["left"]
            else:
                target_word = trial["right"]
            self.the_gui.show_target_word(target_word)
            key_pressed, rt = self.the_gui.show_stimulus(trial["left"], trial["right"], key_list)

            trial_data = [target_word, trial["left"], trial["right"], key_pressed, rt]
            self.data_list.append(trial_data)

    def save_data(self):
        final_data_list = (
            []
        )

        final_data_list.append(
            [
                "participant_id",
                "random_seed",
                "target_word",
                "left_image",
                "right_image",
                "response",
                "correct",
                "rt"
            ]
        )

        for trial_data in self.data_list:
            final_trial_data = [] 

            final_trial_data.append(self.participant_id)

            final_trial_data.append(self.random_seed)

            # add target word to the final trial data
            final_trial_data.append(trial_data[0])

            # add left image to the final trial data
            final_trial_data.append(trial_data[1])

            # add right image to the final trial data
            final_trial_data.append(trial_data[2])

            # add the key that was pressed to the final trial data
            final_trial_data.append(trial_data[3])

            # add whether the key that was pressed was the correct key
            if trial_data[1] == trial_data[0]:
                if trial_data[3] == "f":
                    correct = 1
                else:
                    correct = 0
            elif trial_data[2] == trial_data[0]:
                if trial_data[3] == "j":
                    correct = 1
                else:
                    correct = 0
            else:
                correct = 0

            final_trial_data.append(correct)

            # add the reaction time to the final trial data
            final_trial_data.append(trial_data[4])

            # add the data for the current trial to the full final data list
            final_data_list.append(final_trial_data)

        # create a file with the participant's id number as the file_name, ending with .csv
        filename = f"data/{self.participant_id}.csv"

        # use the csv module to write the full list of lists to the file
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(final_data_list)
