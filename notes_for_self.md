### Delete this later
Stimuli:
| Target | Distractors |
| --- | --- |
| Lion | Tiger Bird Clown |
| Sneaker | Heels Sock pan |
| 4-Square Ball | Soccer ball football Car |
| Chair | Table sink phone |


## Outline
### Tasks
Things to ask about at some point:
- Organizing my project:
  - Making sure that the methods that are supposed to be in exp.py are in exp.py and the ones that're supposed to be in gui.py are in gui.py

Figure out how to conduct multiple trials

- Have a counter for each time a set was accessed
  - somehow keep track of which word has not been hit yet
    - either through a list that corresponds with each of the sets (just have to make sure that the stimulus_list is the same each time)
    - use a dictionary

I think using a dictionary would be best
- Create dictionary method
- Check counter method
- Methods likely to amend:
  - run_experiment
  - present_stimulus_list
  - choose_target_word
  - show_target_word
  - show_stimulus