# Overview of the Stimulus Categorization Experiment
## Introduction to the Experiment
There are different theories that attempt to model how semantic information is represented in the mind. The hierarchical perspective argues that semantic information is organized into a hierarchy consisting of a superordinate, basic, and subordinate layer. Each of these layers have specific categories that range in specificity, typically with the superordinate more general than the basic and subordinate category. For example, the superordinate layer might be mammal, basic layer might be dog, and the subordinate layer might be Golden Retriever. This model can be expanded to describe the relationship within (i.e., Golden retriever versus German Shepard) and between categories (i.e., dog versus shirt). To investigate this view, I hope to create an experiment that will display images on a screen and have the participant click a key, either identifying the target or distractor image. I will record reaction time to get a better understanding of how different superordinate categories are represented.

## Classes
**Exp** - Include the necessary methods needed to run the experiment

**Instruction** - Display the instructions

**Config** - Include constants such as the dimensions of the screen

## Functions/Methods
**show_instructions(self, instruction, end_on_key_press)** - A method that will display the instructions and have an option to get ride of the instructions via a boolean argument.

**run_experiment(self)** - A method that will run the experiment from start to finish. As a result, this method will call other methods in the Exp class and Gui class, such as the show_instructions method.

**save_data(self)** - A method for saving the data. The first row will be a list of strings that specifies that what data is stored in each list element. Then the rest of the data (e.g., participant_id, stimulus, correct, response, rt, etc) will be appended into a final_data_list.

## Code Structure
- `config/` 
  - `config.py` - Congfiguration settings for various parts of the experiment
- `data/` - Stores the participant data from the experiment
- `src/` - Core implementation
  - `exp.py` - Experiment file
  - `gui.py` - Formats the text and images that will be displayed
  - `instructions.txt` - Stores the instructions text
- `stimulus/images/` - Contains all the images used in the experiment
  - `instructions.txt` - Stores the instructions text
- `tests` - Test file
  - `tests.py` - Contains the program that ensures that the program works properly
- `run_experiment.py` - Runs the experiment
