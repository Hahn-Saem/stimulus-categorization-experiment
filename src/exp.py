import random
import datetime
import csv
import os
from config.config import Config

class Exp:
    def __init__(self, the_gui: "Gui") -> None:
        """
        Initializes experiment variables and calls the methods needed to set up and runs the experiment.

        Args:
            the_gui (Gui): an instance of the Gui class that is used to run the experiment.

        Returns:
            None
        """
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

    def create_random_seed(self) -> None:
        """
        Generates a random seed based on the current date and time, and creates a random number generator 
        using that seed.

        Returns:
            None
        """
        self.random_seed = int(self.experiment_start_time.strftime("%Y%m%d%H%M%S%f"))
        self.rng = random.Random(self.random_seed)
    
    def create_participant_id(self) -> None:
        """
        Generates a unique participant ID based on the experiment start time and a random number.

        Returns:
            None
        """
        formatted_datetime = self.experiment_start_time.strftime("%Y%m%d%H%M%S%f")
        random_number = self.rng.randint(100000, 999999)
        self.participant_id = f"{formatted_datetime}_{random_number}"

    def create_instruction_list(self) -> None:
        """
        Creates a list of instructions using the instructions.txt file.

        Returns:
            None
        """

        with open("stimuli/instructions.txt", "r") as file:
            self.instruction_list = [line.strip().replace(".", ".\n") for line in file]

    def create_stimuli_list(self) -> None:
        """
        Adds all the stimuli sets to self.full_stimuli_list. 
        Note: this does NOT add all the images individually, but the folders containing the stimuli sets.

        Returns:
            None
        """
        directory_list = os.listdir("stimuli/images/")

        for set in directory_list:
            curr_dir = os.listdir("stimuli/images/" + set + "/")
            img_set = [img[:-4] for img in curr_dir if not img.startswith(".")]
            self.full_stimuli_list.append(img_set)

    def run_experiment(self) -> None:
        """
        Runs the experiment and saves the data.

        Returns:
            None
        """
        self.the_gui.show_instructions(self.instruction_list[0], True)
        full_stimulus_pairings_list = self.create_stimulus_pairings(self.full_stimuli_list)
        self.run_trials(full_stimulus_pairings_list, Config.test_key_list)
        self.the_gui.show_instructions(self.instruction_list[1], True)
        self.save_data()
        self.the_gui.root.destroy()

    def create_stimulus_pairings(self, stimulus_list: list[list[str]]) -> list[dict[str, str]]: 
        """
        Creates the stimulus pairings, comparing the target word to each distractor image in the same set.
        Additionally, the pairings are counterbalanced, so that the target word appears on the left and 
        right side of the screen an equal number of times across trials, and the order of the pairings 
        is randomized.

        Args:
            stimulus_list (list[list[str]]): a list of lists, where each inner list contains the names of all
            the images in a stimulus set.

        Returns:
            list[dict[str, str]]: a list of dictionaries, where each dictionary represents a stimulus 
            pairing and the side on which it is displayed.
        """
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

        return full_stimulus_pairings_list

    def run_trials(self, full_stimulus_pairings_list: list[dict[str, str]], key_list: list[str]) -> None:
        """
        For each trial, the target word is displayed, each stimulus pairing is presented, and 
        the trial data is recorded.

        Args:
            full_stimulus_pairings_list (list[dict[str, str]]): a list of dictionaries, where each 
            dictionary represents a stimulus pairing and the side on which it is displayed.
            
            key_list (list[str]): a list of strings, where each string represents a key that can be 
            pressed.

        Returns:
            None
        """
        for trial in full_stimulus_pairings_list:
            if trial["left"] in Config.target_word_list:
                target_word = trial["left"]
            else:
                target_word = trial["right"]

            self.the_gui.show_target_word(target_word)
            key_pressed, rt = self.the_gui.show_stimulus(trial["left"], trial["right"], key_list)

            trial_data = [target_word, trial["left"], trial["right"], key_pressed, rt]
            self.data_list.append(trial_data)

    def save_data(self) -> None:
        """
        Saves the data from the experiment in a .csv file.

        Args:
            None

        Returns:
            None
        """
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

            # add the image presented to the left-hand screen to the final trial data
            final_trial_data.append(trial_data[1])

            # add the image presented to the right-hand screen to the final trial data
            final_trial_data.append(trial_data[2])

            # add the key the participant pressed to the final trial data
            final_trial_data.append(trial_data[3])

            # determine whether the key the participant pressed was the correct key
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

            # add whether the key the participant pressed was the correct key
            final_trial_data.append(correct)

            # add the reaction time to the final trial data
            final_trial_data.append(trial_data[4])

            # add the data for the current trial to the full final data list
            final_data_list.append(final_trial_data)

        os.makedirs("data", exist_ok=True)
        
        # create a file with the participant's id number as the file_name, ending with .csv
        filename = f"data/{self.participant_id}.csv"

        # use the csv module to write the full list of lists to the file
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(final_data_list)
