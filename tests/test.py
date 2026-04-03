'''
Print statements for the window

Assert statements to make sure that the data saved


'''

from exp import Exp
import os

def test_window():
    exp = Exp()
    exp.create_window()

    print("The Window should open with the correct title and size.")

def test_instructions():
    exp = Exp()
    exp.create_window()
    exp.show_instructions()

    print("Instructions should appear on the screen with proper formatting.")

def test_stimuli():
    exp = Exp()
    exp.create_window()
    
    exp.show_stimulus("dog.png")

    print("Stimulus shoud appear on the screen.")

def test_run_experiment():
    exp = Exp()
    exp.run_experiment()

    print("Experiment should show instructions, present stimuli, and record responses.")

def test_data_saving():
    exp = Exp()
    exp.run_experiment()

    assert os.path.exists("data.csv"), "Data not saved"

if __name__ == "__main__":
    test_window()
    test_instructions()
    test_stimuli()
    test_run_experiment()
    test_data_saving()
