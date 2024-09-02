# meme-compilation-bot
This project is reddit scraper bot that finds posts and creates a compilation.
## Installation
To install required modules for this project install requirements.txt by running `pip install -r requirements.txt`
## Setup
- Find a short video to be used at the start of the video (I use one that is ~2 seconds) and name it `intro.mp4`
- To use the compilation creator (file is `main.py`) use the video class eg. `Video("discordVideos", 15, 75)`. The arguments are: subreddit (string, remove the "r/"), maximum length of the videos (int, in seconds), and the minimum number of upvotes (int, if you do not want a minimum change this to 0)
- The finished video will be called `video.mp4`!
