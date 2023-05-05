from moviepy.editor import *

class VideoOptimizer():
    def __init__(self, video_path, outputPath):
        self.video = VideoFileClip(video_path)
        self.duration = self.video.duration
        self.size = self.video.size
        self.outputPath = outputPath
        if(self.duration > 59):
            self.background = ColorClip((1080, 1920), (0,0,0), duration=59)
        else:
            self.background = ColorClip((1080, 1920), (0,0,0), duration=self.duration)

    def resize(self):
        width = self.size[0]
        height = self.size[1]
        self.newHeight = 1024 * height / width
        self.video = self.video.resize((1024, self.newHeight))

    def reduce(self):
        self.video = self.video.subclip(0, 59)

    def run(self):
        if(self.duration > 60):
            self.reduce()
        # print(self.size)
        # exit()
        self.resize()
        outputVideo = CompositeVideoClip([self.background, self.video.set_position(('center', 'center'))])
        outputVideo.write_videofile(self.outputPath, codec='libx264', audio_codec="aac")
        self.video.close()

# my_clip = VideoOptimizer(r"test/1.mp4")
# my_clip.run()