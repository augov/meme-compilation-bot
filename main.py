import requests as r
import os
import time
from RedDownloader import RedDownloader as rd
from moviepy.editor import *
#from upload import uploadVideo

class Video:
    def __init__(self, subreddit,maxduration, minupvotes):
        self.count = 1
        self.currentduration = 0
        self.videos = []
        self.subreddit = subreddit
        self.maxduration = maxduration
        self.minupvotes = minupvotes
        self.setup()

    def downloadVideo(self):
        req = r.get(f'https://www.reddit.com/r/{self.subreddit}/random/.json')
        reqjson = req.json()
        if req.status_code == 200:
            reqdata = reqjson[0]["data"]["children"][0]["data"]
            videoduration = reqdata["secure_media"]["reddit_video"]["duration"]
            calculated_duration = self.currentduration + videoduration
            print(calculated_duration)
            print(reqdata["ups"])
            if videoduration > self.maxduration or reqdata["ups"] <= self.minupvotes:
                self.downloadVideo()
                return
            if calculated_duration > 60:
                print("rendering")
                self.render()
                return 
        else:
            time.sleep(5)
            self.downloadVideo()
            return
        url = reqdata["url"]
        try:
            file = rd.Download(url = url , output=f"video/{str(self.count)}", quality = 720)
        except Exception as e:
            print(e)
            self.downloadVideo()
            return
        video = VideoFileClip(f"video/{str(self.count)}.mp4").resize( (1080,1920) )
        self.count += 1
        self.videos.append(video)
        self.currentduration += video.duration
        self.downloadVideo()
        
    def render(self):
        video = concatenate(self.videos, method="compose").resize( (1080,1920) )
        video.write_videofile('video.mp4', fps=24)
        description = open("description.txt", "r")
        #uploadVideo('video.mp4', 'memes i stole from discord', description.read(), 20, ['ylyl', 'you laugh you lose', 'discord memes', 'memes', 'discord'], 'public', False, False)

    def setup(self):
        dir = 'video'
        files = os.listdir(dir)
        for file in files:
            os.remove(f'{dir}/{file}')
        os.rmdir(dir)
        os.makedirs(dir)
        intro = VideoFileClip("intro.mp4")
        self.videos.append(intro)
        self.currentduration += intro.duration
        self.downloadVideo()

Video("discordVideos", 15, 75)