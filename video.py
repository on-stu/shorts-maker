import os
from os.path import expanduser

from VideoOptimizer import VideoOptimizer

inputPath = expanduser("~") + '/Desktop/gags'
outputPath = expanduser("~") + '/Desktop/output/'
videoList = os.listdir(inputPath)
# print(videoList[0])

for i, video in enumerate(videoList):
    if(video[-3: ] == 'mp4'):
        newClip = VideoOptimizer(inputPath + "/" + video, outputPath + str(i) + ".mp4")
        newClip.run()