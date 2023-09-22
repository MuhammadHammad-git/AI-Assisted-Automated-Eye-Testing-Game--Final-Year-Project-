# AI Assisted Automated Eye Testing Game (Final Year Project) "SNELL"
## It is a completely Automated Eye Testing Machine. It is a game. It uses Voice Recognition AI! It is fun, interactive and addicting to play. All of it runs on the microcontroller Raspberry pi 4B!
This is my most innovative and fun work. A project that encompasses all of my work and showcases my coding skills!

*Here is a link to the wonderfull ceremony and sadly my last day at university!
https://www.linkedin.com/posts/muhammad-hammad-87787421a_four-years-and-they-went-like-that-mashallah-activity-7070119934269210624-aq94?utm_source=share&utm_medium=member_desktop*

# Game Details
## Animation:
The Game includes a wooden board (Created frame by frame in Paint *Every animation is made like this*) placed in a forest environment that pops up and digs down in the ground! The letters appear on the board and the appearance, background and font of the letters are specific to the requirement for an eye test! The Letters displayed are Random and Are displayed randomly anywhere but only on the ground part of the forest!
There is grass animation as well to show multithreading.
## Audio, Model and the user:
Audio of the user is taken by either a headphone or microphone. The audio first passes through the sliding window algorithm that inputs the audio to the model in 1 sec samples. if the first window of audio does not produce the required result then the audio window is moved ahead 0.5 seconds and another audio sample is passed! Until all the requirement are met only then the model output is used! All this is to ensure that the patient has a seemless experience, i.e allowing him/her to say too early or too late or even repeat a letter without causing any issues.
## The Result:
At the end of the eye test, keeping in view the number of mistakes made by the patient in guessing letters, a result is generated that consists of a layman term category, visual acuity and approximate range of diopter of lens. The layman category is defined by taking inspiration from WHO, Visual acuity is guessed on the bases of a defined formula while Diopter lens value is guessed by a data set. The data set consists of 400 eye tests each taken by ourself by visiting General Hospital Lahore's Ophthalmology ward. Based on this data set we guess the approximate lens power the user can have! Because this is soo subjective it was unable to be guessed with a lower range!
## Game Optimizations:
Game is Optimized for Raspberry pi 4B. Can be run on any display with a resolution of 800x600 upto 4k. Any screen resolution below losses quality as game elements are compressed too much to fit into the screen. 
## Potiental Bugs (Library dependent)
Pygames library on Raspberry pi struggles with scaling issues and has bugs. I have handled the resolution in such a way as to reduce such bugs as much as possible. _These bugs only happen randomly on some runs_.

Some bugs include:
- unable to scale properly
- unable to sometimes remove default black background on transparent png's.

# SHOTS:

## Menu Screen:
![Updated Menu (Square Screen)](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/cf8c9b5e-57ef-44d0-86c4-0b0290cc9ff5)
## Instruction Screen:
![Instruction Screen](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/2528545c-5295-45e9-80b4-2b4e356642b6)

## Game_Progression:

![Gameshot1](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/22350745-79e9-4a34-8587-99b22e9b39d1)

![Gameshot2](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/3a5f3f44-8628-40c1-baee-06f380243c24)

![Screenshot 2023-05-06 113850](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/8d144d37-1a4f-4e9d-a4aa-4cf887dadcce)

![Screenshot 2023-05-06 114025](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/72f8cf69-1978-4795-9335-9621a9551929)

![Gameshot3](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/e133b332-1bb9-4d3f-9b0f-505ecde0d827)

## RESULTS SCREEN!
![Result Screen](https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/7973c7bc-d5e9-4bd4-9594-f496e00fade3)


# DEMO

## Game Demo without any voice input
https://github.com/MuhammadHammad-git/AI-Assisted-Automated-Eye-Testing-Game--Final-Year-Project-/assets/74261526/9e9cae16-920a-4973-a69d-c4f44d923e06

## Realtime With Patient
https://drive.google.com/file/d/1WJ-i7jxUeieNWjcf0R-orHxnQ-HDCrY3/view?usp=drive_link
*Here Letters that blink green are recognized while those in red are missed by the model!
Here, we can clearly observe that even in such a noisy environment our Model is working with an accuracy of more than 95%!
This was a huge accompolishment for us as all of the data was collected by us through Audio recording! This audio data set is not available for free anywhere on the web!
There are 5 Letters that appear on the screen T O Z F L. We collected 160 to 170 audio samples for each letter.
The model we used here is trained using CNN while Google Teachable machines model was used as a prototype and benchmark to assess our model*
