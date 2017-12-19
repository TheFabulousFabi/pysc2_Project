# pysc2_Project
Repository for the Starcraft 2 API pysc2

# Preface

This project is part of the bachelor degree program at the University of Applied Sciences in Fulda, Germany.
Our goal is to extract data from Starcraft 2 matches on the basis of [pysc2](https://github.com/deepmind/pysc2 "pysc2") to use it later for machine learning methods.
Therefore we will create simple [bots](https://github.com/TheFabulousFabi/pysc2_Project/tree/master/bots "bots") to test the pysc2-interface and collect simple datasets. In addition to this we want
to collect data from Starcraft 2 [replays](https://github.com/TheFabulousFabi/pysc2_Project/tree/master/replay "replays"), as well as games with real players.

The features we are planning to extract are:
* race
* unit counts
* building counts
* tech status
* resources
* apm
* win-lose information at the end of a match

# Bots

We built several [bots](https://github.com/TheFabulousFabi/pysc2_Project/tree/master/bots "bots") to generate own datasets. Currently there are four different types of executable scenarios:
* marines trying to kill roaches
* marines attacking the enemy base
* marines collecting mineral shards
* marines moving to beacons

# Replays

**Downloadscript for replays:**

In fact, that we wanted to learn with the best replays we created a script to download 
pro player replays from the website http://sc2replaystats.com

First of all the script sorts by players with master or grandmaster rank. After that we check
if there is a download section. If there is a download section the script starts the download.

After this it automatically moves to the next link and repeats the check.

The script ignores lower ranked replays, so we secure that our 
artificial neural networks gets the best replays to learn with.

With the newest version of the script it is now possible to select the game version and minimum league for the replay files.
In addition to this there is an option to print the URLs of the replays in a txt-file.

Until further notice the work on the downloadscript is finished.

**Data extraction with replays:**

To extract data from replays we tried to use two different programs which are provided by [pysc2](https://github.com/deepmind/pysc2 "pysc2"):
* play.py (runs the replay visually in realtime)
* replay_actions.py (returns all actions within the replay in the console)

However we had some issues with running them on different systems as you can see in our progression.
With "replay_actions.py" we managed to extract the data from a replay at a given time with a so called "obs"-variable.
As far as known it is unfortunately not subscriptable, so the output has to be searched manually for specific units.

# Progression

**Data extraction with replays:**



# ToDo List

* replay analysis
  - [x] extract data from a given state of a match
* optimizing the downloadscript
  - [x] reset the console after execution
  - [x] print the links into a txt-file
* expanding documentation
  - [x] add ToDo List
  - [x] add more information on the status of the downloadscript
  - [x] add more information on the replay analysis ("obs"-variable)
  - [x] add more information about what we already tried but didn't work (progression)
