# Nostalgia Video Automation

The goal of this project was to create an python app for automating minecraft short nostalgia content.
The project uses moviepy to edit a simple video consisting of nostalgic music and a motivational message.
Videos generated by this script were posted on the [NostalgiaPill](https://www.youtube.com/@NostalgiaPill404) YouTube channel.

## ⚙️ Setup

**Python** is required to run this software.
Project uses **moviepy** be sure to install it via **pip** using the following command:
```sh
pip install moviepy
```

## 💬 Messages for videos

Messages dispalyed on videos are kept inside the ``Data/Assets/Prompts`` directory.
To create new messages for the videos modify the ``OneLiners.txt`` file. The new message should be short and should follow this pattern:

```
scenery
mood
text message one
text message two
```

### 🌇 Scenery
The scenery parameter picks the type of background image used in the video. It coresponds to the directory name inside of ``Data/Assets/Screens``.

List of aviable sceneries:
```
Day
Night
Cave
House
Rain
```

### 🌆 Mood
The mood parameter picks the type of music used in the video. It coresponds to the directory name inside of ``Data/Assets/Music Cut``. The music also defines the length of the video. For example if the music is 8 seconds long the video will also be 8 seconds long. Be sure to add music inside the music folder as due to possible copyright issues I didin't put any music in.

List of aviable moods (not aviable due to copyright should be filled manually):
```
Happy
Motivation
Nostalgic
Sad
```

## 🎥 Creating the video
To create the video write this command inside a terminal:
```sh
python VideoManager.py
```
This will launch the video manager. The program will ask you for the action you want to perform. Write this command to start the video creation:
```sh
oneliner
```
Creating the video will remove the used message from ``OneLiners.txt``. Be sure to refill the prompts from time to time.
After the video finishes editing it will appear inside ``Final Clips`` folder.

