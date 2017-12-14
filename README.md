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

# Replays

Downloadscript for Replays:

In fact, that we wanted to learn with the best Replay's we created a script to download 
pro Player replay's from the website http://sc2replaystats.com

The script first of all sorts for Master or Grandmaster Player. After that we check
if there is a download section. If there is a download section the Script starts the download.

After this it automaticly goes to the next link and repeat the check.

The script ignoeres lower ranked Replay's, so we secure that our 
artificially neural networks get's the best replay's to learn.
