# Overview of the Stimulus Categorization Experiment
## Introduction to the Experiment
There are different theories that attempt to model how semantic information is represented in the mind. The hierarchical perspective argues that semantic information is organized into a hierarchy consisting of a superordinate, basic, and subordinate layer. Each of these layers have specific categories that range in specificity, with the superordinate being more general than the basic and subordinate category. For example, the superordinate layer might be mammal, basic layer might be dog, and the subordinate layer might be Golden Retriever. This model can be expanded to describe the relationship within (i.e., Golden retriever versus German Shepard) and between categories (i.e., dog versus shirt). 

To investigate this view, I created an experiment that tests whether participants will respond more slowly when the distractor image is semantically similar to the target image. 
Participants are shown a target word followed by two side-by-side images:
- A target image
- A distractor image

The participant must identify the target image that corresponds to the target word as quickly and accurately as possible, using the 'f' key to indicate that the target image appeared on the left hand of the screen and the 'j' key to indicate that the target image appeared on the right hand of the screen.

For example:
- `dog` vs `cat` -> expect a slower reaction time
- `dog` vs `bird` -> expect a moderation reaction time
- `dog` vs `phone` -> expect fast reaction time

## Classes
**Exp** - Includes the necessary methods needed to run the experiment and saves the data

**Gui** - Contains the methods needed to display the stimuli and text on the screen

**Config** - Holds constants that is accessed by other files

## Functions/Methods
**show_instructions(self, instruction, end_on_key_press, extra_delay)** - A method that will display the instructions, includes an option to get rid of the instructions via a boolean argument, and allows for an additionaly delay before ending the instruction display.

**run_experiment(self)** - A method that will run the experiment from start to finish. As a result, this method will call other methods in the Exp class and Gui class.

**create_stimulus_pairings(self, stimulus_list)** - Creates the stimulus pairings, comparing the target word to each distractor image in the same set. Additionally, the pairings are counterbalanced, so that the target word appears on the left and right side of the screen an equal number of times across trials, and the order of the pairings is randomized. 

**run_trials(self, full_stimulus_pairings_list, key_list)** - Displays the target word, then presents the stimulus pairing, and lastly records the trial data.

**save_data(self)** - A method for saving the data. The first row will be a list of strings that specifies that what data is stored in each list element. Then the rest of the data (e.g., participant_id, stimulus, correct, response, rt, etc) will be appended into a final_data_list.

## Installation
```
# Install the required dependencies
pip install -r requirements.txt

# Run the Experiment
python run_experiment.py
```

## Testing
The user should expect to see the experiment instructions on the screen after opening the experiment (via `python run_experiment.py`) in the terminal. Per the instructions, the participant will be able to begin the experiment by using the SPACE bar. During the experiment, two side-by-side images (a target image and a distractor image) should appear, and the participant should be able to identify the target image using the 'f' or 'j' key. After making a response, the next trial (a target word followed by a pair of images) should appear until the end of the experiment. Finally, a message notifying the participant that they have completed the experiment should appear on the screen. To exit out of the program, the user will click the SPACE bar.

To summarize, the program will run as anticipated if the instructions appear on the screen at the beginning and at the end of the experiment, a target word is presented, a pair of images appear on the screen, and the program responds accordingly to the key that is pressed.

## Code Structure
- `config/` 
  - `__init__.py` - Empty file that marks `config` as a Python package.
  - `config.py` - Congfiguration settings for various parts of the experiment.
- `data/` - Stores the participant data from the experiment.
- `src/` - Core implementation.
  - `exp.py` - Experiment file.
  - `gui.py` - Formats the text and images that will be displayed.
- `stimuli/` - Holds the images and instructions file.
  - `images/` - Contains the four stimuli sets.
    - `set1/` - Stimuli set 1. Target word is lion.
    - `set2/` - Stimuli set 2. Target word is sneaker.
    - `set3/` - Stimuli set 3. Target word is red ball.
    - `set4/` - Stimuli set 4. Target word is chair.
  - `instructions.txt` - Stores the instructions text
- `requirements.txt` - Notes any libraries used in the program beyond the standard Python library.
- `run_experiment.py` - Runs the experiment.