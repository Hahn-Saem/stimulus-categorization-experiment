# Hahn-Saem Lee | BCOG 200 Final Project
## Description of my planned project (1)

For my final project, I hope to measure the reaction time for identifying a target stimulus compared to several distractor items. I imagine the experiment will begin by having the participants view an instructions page. Next, a target word will be presented, followed by a side-by-side display containing the target image and a distractor image. Participants will then press the key corresponding to the side of the screen where the target image appears (i.e., press “F” if the target image appears on the left side of the screen and “J” if it appears on the right). This process will repeat several times for different superordinate categories, such as mammals, clothes, etc. Another possible extension of this project would be to turn the experiment into a website or application. That way, participants can conduct this experiment at home, on a computer, or on a mobile device. 

To expand on the details of the experiment, there will be a set of distractor images that vary in their semantic relatedness to the target image. For example, if lion is the target image, the distractor images might be tiger, bird, and chair. Tiger is the most semantically related to lion, followed by bird and chair. Ideally, these images would be centered, similar in size, and on the same background. I will try my best to find images or, perhaps, find a way to alter the images to meet these criteria. Additionally, I plan to counterbalance these photos, ensuring that each image appears the same number of times and appears on either the left or right side of the screen an equal amount of times.


## Description of functions (2 a, b, c)
Other than the main function, I plan to have a function that will run the experiment. The function will display the target as a word first, then show the target image and distractor images, abiding by the details provided in the second paragraph of the project description.

I also plan to include a function that gets the next set of category items and returns them. These set of items will then be passed as an argument to the function that runs the experiment, which is also the function described in the previous paragraph.

A third function I hope to include is a function that will record the time it takes to identify the target image. That is, the time it takes for the participant to click on a key when the target and the distractor image are displayed side-by-side on the screen. I might also keep track of whether the participant chose the correct item in this function.

### Helpful links for myself
https://bcog200.netlify.app/CH20/

https://www.jspsych.org/latest/tutorials/rt-task/

https://www.psychopy.org/

https://github.com/Hahn-Saem/stimulus-categorization-experiment/blob/main/README.md