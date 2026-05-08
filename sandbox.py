import random
import itertools

images = ["chair", "table", "lion"]
target_word = "popsicle"

screen_sides = ["left", "right"]

pairings_list = []
for image in images:
    pairings_list.append((target_word, image))

# words within the list vs each other
for image1, image2 in itertools.combinations(images, 2):
    pairings_list.append((image1, image2))

num_pairings = len(pairings_list)
print(num_pairings)
num_sides = len(screen_sides)

if num_pairings % 2 == 1:
    images_per_side = (num_pairings // num_sides) + 1
else:
    images_per_side = num_pairings // num_sides

screen_sides = screen_sides * images_per_side * 2

print("----------")
print(len(screen_sides))

random.shuffle(pairings_list)
random.shuffle(screen_sides)

print(screen_sides)
print(pairings_list)

# for image, side in zip(images, screen_sides):
#     print(image, side)


'''
Method 1:
Do what I did above (shuffle within a set)
But then I just put the target image on the opposite side
^ this is my order

Then I just need to randomize the output
'''
'''
Method 2:
Or put all the stimuli into one list with the side
Shuffle the entire list
Use an if-statement to see which set we're using and where the target word is
Then put the target image on the opposite side
'''
'''
An extension might be then also randomly comparing the image within a set to each other

Factorial seems like the best way to randomize the inputs into each part of the side
But how do I make sure that the image appears once on each side? 
Or just randomize it?
'''

'''
Compare each of the items within the set to each other
Shuffle screen_sides
append to a display the word pairing list

OR

Compare each of the items within the set to each other
Append to a list_output
Repeat for each of the sets
Shuffle the list_output
Shuffle screen_size
'''

'''
Tasks:
- present_stimulus_list in exp.py
- run_experiment in exp.py, particularly running the experiment and saving the data
'''